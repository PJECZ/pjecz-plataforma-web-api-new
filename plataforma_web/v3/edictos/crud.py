"""
Edictos v3, CRUD (create, read, update, and delete)
"""
from datetime import date
from typing import Any
from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError

from ...core.autoridades.models import Autoridad
from ...core.edictos.models import Edicto
from ..autoridades.crud import get_autoridad, get_autoridad_with_clave
from ..distritos.crud import get_distrito, get_distrito_with_clave


def get_edictos(
    db: Session,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    anio: int = None,
    fecha: date = None,
) -> Any:
    """Consultar los edictos activos"""
    consulta = db.query(Edicto)
    if autoridad_id is not None:
        autoridad = get_autoridad(db, autoridad_id)
        consulta = consulta.filter_by(autoridad_id=autoridad.id)
    elif autoridad_clave is not None:
        autoridad = get_autoridad_with_clave(db, autoridad_clave)
        consulta = consulta.filter_by(autoridad_id=autoridad.id)
    elif distrito_id is not None:
        distrito = get_distrito(db, distrito_id)
        consulta = consulta.join(Autoridad).filter(Autoridad.distrito_id == distrito.id)
    elif distrito_clave is not None:
        distrito = get_distrito_with_clave(db, distrito_clave)
        consulta = consulta.join(Autoridad).filter(Autoridad.distrito_id == distrito.id)
    if fecha is not None:
        consulta = consulta.filter(Edicto.fecha == fecha)
    elif anio is not None:
        if 1900 <= anio <= date.today().year:
            consulta = consulta.filter(Edicto.fecha >= date(anio, 1, 1)).filter(Edicto.fecha <= date(anio, 12, 31))
        else:
            raise MyNotValidParamError("El año no es válido")
    return consulta.filter_by(estatus="A").order_by(Edicto.id.desc())


def get_edicto(db: Session, edicto_id: int) -> Edicto:
    """Consultar un edicto por su id"""
    edicto = db.query(Edicto).get(edicto_id)
    if edicto is None:
        raise MyNotExistsError("No existe ese edicto")
    if edicto.estatus != "A":
        raise MyIsDeletedError("No es activo ese edicto, está eliminado")
    return edicto
