"""
REDAM (Registro Estatal de Deudores Alimentarios Morosos) v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_user
from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false
from lib.fastapi_pagination_datatable import DataTablePage, datatable_page_success_false

from .crud import get_redams, get_redam
from .schemas import RedamOut, OneRedamOut

redam = APIRouter(prefix="/v3/redam", tags=["redam"])


@redam.get("", response_model=CustomPage[RedamOut])
async def listado_redam(
    db: DatabaseSession,
    current_user: Annotated[Usuario, Depends(get_current_user)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    nombre: str = None,
    expediente: str = None,
):
    """Listado de Deudores Alimentarios Morosos"""
    try:
        resultados = get_redams(
            db=db,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            nombre=nombre,
            expediente=expediente,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@redam.get("/datatable", response_model=DataTablePage[RedamOut])
async def listado_redam_datatable(
    db: DatabaseSession,
    current_user: Annotated[Usuario, Depends(get_current_user)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    nombre: str = None,
    expediente: str = None,
):
    """Listado de Deudores Alimentarios Morosos para DataTable"""
    try:
        resultados = get_redams(
            db=db,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            nombre=nombre,
            expediente=expediente,
        )
    except MyAnyError as error:
        return datatable_page_success_false(error)
    return paginate(resultados)


@redam.get("/{redam_id}", response_model=OneRedamOut)
async def detalle_redam(
    db: DatabaseSession,
    current_user: Annotated[Usuario, Depends(get_current_user)],
    redam_id: int,
):
    """Detalle de una Deudor Alimentario Moroso a partir de su id"""
    try:
        deudor = get_redam(db, redam_id)
    except MyAnyError as error:
        return OneRedamOut(success=False, message=str(error))
    return OneRedamOut.from_orm(deudor)
