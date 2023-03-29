"""
REPSVM Agresores v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError

from ...core.repsvm_agresores.models import RepsvmAgresor


def get_repsvm_agresores(
    db: Session,
) -> Any:
    """Consultar los agresores activos"""
    consulta = db.query(RepsvmAgresor)
    return consulta.filter_by(estatus="A").order_by(RepsvmAgresor.id)


def get_repsvm_agresor(db: Session, repsvm_agresor_id: int) -> RepsvmAgresor:
    """Consultar un agresor por su id"""
    repsvm_agresor = db.query(RepsvmAgresor).get(repsvm_agresor_id)
    if repsvm_agresor is None:
        raise MyNotExistsError("No existe ese agresor")
    if repsvm_agresor.estatus != "A":
        raise MyIsDeletedError("No es activo ese agresor, está eliminado")
    return repsvm_agresor
