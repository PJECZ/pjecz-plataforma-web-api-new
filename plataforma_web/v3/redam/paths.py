"""
REDAM (Registro Estatal de Deudores Alimentarios Morosos) v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_user
from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false
from lib.fastapi_pagination_datatable import DataTablePage, datatable_page_success_false

from .crud import get_redam, get_redams
from .schemas import OneRedamOut, RedamOut

redam = APIRouter(prefix="/v3/redam", tags=["redam"])


@redam.get("/datatable", response_model=DataTablePage[RedamOut])
async def listado_redam_datatable(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_user)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    nombre: str = None,
    expediente: str = None,
):
    """Listado de Deudores Alimentarios Morosos para DataTable"""
    draw = request.query_params.get("draw")
    if draw is None or not draw.isdigit() or int(draw) < 1:
        return datatable_page_success_false("Invalid request")
    try:
        resultados = get_redams(
            database=database,
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


@redam.get("/paginado", response_model=CustomPage[RedamOut])
async def listado_redam(
    database: Annotated[Session, Depends(get_db)],
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
            database=database,
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


@redam.get("/{redam_id}", response_model=OneRedamOut)
async def detalle_redam(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_user)],
    redam_id: int,
):
    """Detalle de un redam a partir de su id"""
    try:
        resultado = get_redam(database=database, redam_id=redam_id)
    except MyAnyError as error:
        return OneRedamOut(success=False, error=error)
    return OneRedamOut.from_orm(resultado)
