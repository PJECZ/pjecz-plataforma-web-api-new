"""
Sentencias v3, CRUD (create, read, update, and delete)
"""

from datetime import date
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_expediente
from plataforma_web.core.autoridades.models import Autoridad
from plataforma_web.core.sentencias.models import Sentencia
from plataforma_web.v3.autoridades.crud import get_autoridad, get_autoridad_with_clave
from plataforma_web.v3.distritos.crud import get_distrito, get_distrito_with_clave
from plataforma_web.v3.materias_tipos_juicios.crud import get_materia_tipo_juicio


def get_sentencias(
    database: Session,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    expediente: str = None,
    fecha: date = None,
    fecha_desde: date = None,
    fecha_hasta: date = None,
    materia_tipo_juicio_id: int = None,
    sentencia: str = None,
) -> Any:
    """Consultar las sentencias"""
    consulta = database.query(Sentencia)
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
    if fecha is not None:
        consulta = consulta.filter(Sentencia.fecha == fecha)
    else:
        if fecha_desde is not None:
            consulta = consulta.filter(Sentencia.fecha >= fecha_desde)
        if fecha_hasta is not None:
            consulta = consulta.filter(Sentencia.fecha <= fecha_hasta)
    if expediente is not None:
        try:
            expediente = safe_expediente(expediente)
        except (IndexError, ValueError) as error:
            raise MyNotValidParamError("El expediente no es válido") from error
        consulta = consulta.filter_by(expediente=expediente)
    if materia_tipo_juicio_id is not None:
        materia_tipo_juicio = get_materia_tipo_juicio(database, materia_tipo_juicio_id)
        consulta = consulta.filter_by(materia_tipo_juicio_id=materia_tipo_juicio.id)
    if sentencia is not None:
        try:
            sentencia = safe_expediente(sentencia)
        except (IndexError, ValueError) as error:
            raise MyNotValidParamError("La sentencia no es válida") from error
        consulta = consulta.filter_by(sentencia=sentencia)
    return consulta.filter(Sentencia.estatus == "A").order_by(Sentencia.id.desc())


def get_sentencia(database: Session, sentencia_id: int) -> Sentencia:
    """Consultar una sentencia por su id"""
    sentencia = database.query(Sentencia).get(sentencia_id)
    if sentencia is None:
        raise MyNotExistsError("No existe ese sentencia")
    if sentencia.estatus != "A":
        raise MyIsDeletedError("No es activo ese sentencia, está eliminado")
    return sentencia
