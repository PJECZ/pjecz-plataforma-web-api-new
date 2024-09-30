"""
Ubicaciones de Expedientes v3, CRUD (create, read, update, and delete)
"""

from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_expediente
from plataforma_web.core.ubicaciones_expedientes.models import UbicacionExpediente
from plataforma_web.v3.autoridades.crud import get_autoridad, get_autoridad_with_clave


def get_ubicaciones_expedientes(
    database: Session,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    expediente: str = None,
) -> Any:
    """Consultar las ubicaciones de expedientes activas"""
    consulta = database.query(UbicacionExpediente)
    if autoridad_id is not None:
        autoridad = get_autoridad(database, autoridad_id)
        consulta = consulta.filter_by(autoridad_id=autoridad.id)
    elif autoridad_clave is not None and autoridad_clave != "":
        autoridad = get_autoridad_with_clave(database, autoridad_clave)
        consulta = consulta.filter_by(autoridad_id=autoridad.id)
    if expediente is not None:
        try:
            expediente = safe_expediente(expediente)
        except (IndexError, ValueError) as error:
            raise MyNotValidParamError("El expediente no es válido") from error
        consulta = consulta.filter_by(expediente=expediente)
    return consulta.filter_by(estatus="A").order_by(UbicacionExpediente.expediente)


def get_ubicacion_expediente(database: Session, ubicacion_expediente_id: int) -> UbicacionExpediente:
    """Consultar una ubicacion de expediente por su id"""
    ubicacion_expediente = database.query(UbicacionExpediente).get(ubicacion_expediente_id)
    if ubicacion_expediente is None:
        raise MyNotExistsError("No existe ese ubicacion de expediente")
    if ubicacion_expediente.estatus != "A":
        raise MyIsDeletedError("No es activo ese ubicacion de expediente, está eliminado")
    return ubicacion_expediente
