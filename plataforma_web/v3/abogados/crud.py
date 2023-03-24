"""
Abogados v3, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError

from ...core.abogados.models import Abogado


def get_abogados(db: Session) -> Any:
    """Consultar los abogados activos"""
    consulta = db.query(Abogado)
    return consulta.filter_by(estatus="A").order_by(Abogado.id)


def get_abogado(db: Session, abogado_id: int) -> Abogado:
    """Consultar un abogado por su id"""
    abogado = db.query(Abogado).get(abogado_id)
    if abogado is None:
        raise MyNotExistsError("No existe ese abogado")
    if abogado.estatus != "A":
        raise MyIsDeletedError("No es activo ese abogado, está eliminado")
    return abogado
