"""
Autoridades v3, CRUD (create, read, update, and delete)
"""

from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_clave
from plataforma_web.core.autoridades.models import Autoridad
from plataforma_web.v3.distritos.crud import get_distrito, get_distrito_with_clave
from plataforma_web.v3.materias.crud import get_materia, get_materia_with_clave


def get_autoridades(
    database: Session,
    distrito_id: int = None,
    distrito_clave: str = None,
    es_cemasc: bool = None,
    es_creador_glosas: bool = None,
    es_defensoria: bool = None,
    es_jurisdiccional: bool = None,
    es_notaria: bool = None,
    es_organo_especializado: bool = None,
    materia_id: int = None,
    materia_clave: str = None,
) -> Any:
    """Consultar las autoridades"""
    consulta = database.query(Autoridad)
    if distrito_id is not None:
        distrito = get_distrito(database, distrito_id)
        consulta = consulta.filter_by(distrito_id=distrito.id)
    elif distrito_clave is not None and distrito_clave != "":
        distrito = get_distrito_with_clave(database, distrito_clave)
        consulta = consulta.filter_by(distrito_id=distrito.id)
    if es_cemasc is not None:
        consulta = consulta.filter_by(es_cemasc=es_cemasc)
    if es_creador_glosas is True:
        consulta = consulta.filter(
            Autoridad.organo_jurisdiccional.in_(["PLENO O SALA DEL TSJ", "TRIBUNAL DE CONCILIACION Y ARBITRAJE"])
        )
    if es_defensoria is not None:
        consulta = consulta.filter_by(es_defensoria=es_defensoria)
    if es_jurisdiccional is not None:
        consulta = consulta.filter_by(es_jurisdiccional=es_jurisdiccional)
    if es_notaria is not None:
        consulta = consulta.filter_by(es_notaria=es_notaria)
    if es_organo_especializado is not None:
        consulta = consulta.filter_by(es_organo_especializado=es_organo_especializado)
    if materia_id is not None:
        materia = get_materia(database, materia_id)
        consulta = consulta.filter_by(materia_id=materia.id)
    elif materia_clave is not None and materia_clave != "":
        materia = get_materia_with_clave(database, materia_clave)
        consulta = consulta.filter_by(materia_id=materia.id)
    return consulta.filter_by(estatus="A").order_by(Autoridad.clave)


def get_autoridad(database: Session, autoridad_id: int) -> Autoridad:
    """Consultar una autoridad por su id"""
    autoridad = database.query(Autoridad).get(autoridad_id)
    if autoridad is None:
        raise MyNotExistsError("No existe ese autoridad")
    if autoridad.estatus != "A":
        raise MyIsDeletedError("No es activo ese autoridad, está eliminado")
    return autoridad


def get_autoridad_with_clave(database: Session, clave: str) -> Autoridad:
    """Consultar una autoridad por su clave"""
    try:
        clave = safe_clave(clave)
    except ValueError as error:
        raise MyNotValidParamError(str(error)) from error
    autoridad = database.query(Autoridad).filter_by(clave=clave).first()
    if autoridad is None:
        raise MyNotExistsError("No existe ese autoridad")
    if autoridad.estatus != "A":
        raise MyIsDeletedError("No es activo ese autoridad, está eliminado")
    return autoridad
