"""
REVSPM Agresores v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_user
from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false
from lib.fastapi_pagination_datatable import DataTablePage, datatable_page_success_false

from .crud import get_repsvm_agresores
from .schemas import RepsvmAgresorOut

repsvm_agresores = APIRouter(prefix="/v3/repsvm_agresores", tags=["repsvm agresores"])


@repsvm_agresores.get("", response_model=CustomPage[RepsvmAgresorOut])
async def listado_repsvm_agresores(
    db: DatabaseSession,
    current_user: Annotated[Usuario, Depends(get_current_user)],
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
    current_user: Annotated[Usuario, Depends(get_current_user)],
    distrito_id: int = None,
    distrito_clave: str = None,
    nombre: str = None,
):
    """Listado de agresores para DataTable"""
    try:
        resultados = get_repsvm_agresores(
            db=db,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            nombre=nombre,
        )
    except MyAnyError as error:
        return datatable_page_success_false(error)
    return paginate(resultados)
