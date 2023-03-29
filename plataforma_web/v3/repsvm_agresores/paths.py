"""
REVSPM Agresores v3, rutas (paths)
"""
from fastapi import APIRouter
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false
from lib.fastapi_pagination_datatable import DataTablePage, datatable_page_success_false

from .crud import get_repsvm_agresores, get_repsvm_agresor
from .schemas import RepsvmAgresorOut, OneRepsvmAgresorOut

repsvm_agresores = APIRouter(prefix="/v3/repsvm_agresores", tags=["repsvm agresores"])


@repsvm_agresores.get("", response_model=CustomPage[RepsvmAgresorOut])
async def listado_repsvm_agresores(
    db: DatabaseSession,
    distrito_id: int = None,
    distrito_clave: str = None,
    nombre: str = None,
):
    """Listado de agresores"""
    try:
        resultados = get_repsvm_agresores(
            db=db,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            nombre=nombre,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@repsvm_agresores.get("/datatable", response_model=DataTablePage[RepsvmAgresorOut])
async def listado_repsvm_agresores_datatable(
    db: DatabaseSession,
):
    """Listado de agresores para DataTable"""
    try:
        resultados = get_repsvm_agresores(db=db)
    except MyAnyError as error:
        return datatable_page_success_false(error)
    return paginate(resultados)


@repsvm_agresores.get("/{repvm_agresor_id}", response_model=OneRepsvmAgresorOut)
async def detalle_repvm_agresor(
    db: DatabaseSession,
    repvm_agresor_id: int,
):
    """Detalle de un agresor a partir de su id"""
    try:
        repvm_agresor = get_repsvm_agresor(db=db, repvm_agresor_id=repvm_agresor_id)
    except MyAnyError as error:
        return OneRepsvmAgresorOut(success=False, message=str(error))
    return OneRepsvmAgresorOut.from_orm(repvm_agresor)
