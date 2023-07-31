"""
Tesis Jurisprudencias v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError

from ...core.autoridades.models import Autoridad
from ...core.tesis_jurisprudencias.models import TesisJurisprudencia
from ..autoridades.crud import get_autoridad, get_autoridad_with_clave
from ..distritos.crud import get_distrito, get_distrito_with_clave
from ..epocas.crud import get_epoca
from ..materias.crud import get_materia, get_materia_with_clave


def get_tesis_jurisprudencias(
    database: Session,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    epoca_id: int = None,
    materia_id: int = None,
    materia_clave: str = None,
) -> Any:
    """Consultar las tesis jurisprudencias activas"""
    consulta = database.query(TesisJurisprudencia)
    if autoridad_id is not None:
        autoridad = get_autoridad(database, autoridad_id)
        consulta = consulta.filter_by(autoridad_id=autoridad.id)
    elif autoridad_clave is not None and autoridad_clave != "":
        autoridad = get_autoridad_with_clave(database, autoridad_clave)
        consulta = consulta.filter_by(autoridad_id=autoridad.id)
    elif distrito_id is not None:
        distrito = get_distrito(database, distrito_id)
        consulta = consulta.join(Autoridad).filter(Autoridad.distrito_id == distrito.id)
    elif distrito_clave is not None and distrito_clave != "":
        distrito = get_distrito_with_clave(database, distrito_clave)
        consulta = consulta.join(Autoridad).filter(Autoridad.distrito_id == distrito.id)
    if epoca_id is not None:
        epoca = get_epoca(database, epoca_id)
        consulta = consulta.filter_by(epoca_id=epoca.id)
    if materia_id is not None:
        materia = get_materia(database, materia_id)
        consulta = consulta.filter_by(materia_id=materia.id)
    elif materia_clave is not None and materia_clave != "":
        materia = get_materia_with_clave(database, materia_clave)
        consulta = consulta.filter_by(materia_id=materia.id)
    return consulta.filter_by(estatus="A").order_by(TesisJurisprudencia.id)


def get_tesis_jurisprudencia(database: Session, tesis_jurisprudencia_id: int) -> TesisJurisprudencia:
    """Consultar una tesis jurisprudencia por su id"""
    tesis_jurisprudencia = database.query(TesisJurisprudencia).get(tesis_jurisprudencia_id)
    if tesis_jurisprudencia is None:
        raise MyNotExistsError("No existe ese tesis jurisprudencia")
    if tesis_jurisprudencia.estatus != "A":
        raise MyIsDeletedError("No es activo ese tesis jurisprudencia, está eliminado")
    return tesis_jurisprudencia
