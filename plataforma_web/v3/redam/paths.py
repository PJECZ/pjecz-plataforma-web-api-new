"""
REDAM (Registro Estatal de Deudores Alimentarios Morosos) v3, rutas (paths)
"""

from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_userdev, get_current_username
from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false
from lib.fastapi_pagination_datatable import DataTable, custom_datatable_sucess_false
from lib.limiter import limiter
from plataforma_web.v3.redam.crud import get_redam, get_redams
from plataforma_web.v3.redam.schemas import ItemRedamOut, OneRedamOut

redam = APIRouter(prefix="/v3/redam", tags=["redam"])


@redam.get("/datatable", response_model=DataTable[ItemRedamOut])
@limiter.limit("40/minute")
async def listado_redam_datatable(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    nombre: str = None,
    expediente: str = None,
):
    """DataTable de Deudores Alimentarios Morosos"""
    # draw = request.query_params.get("draw")
    # if draw is None or not draw.isdigit() or int(draw) < 1:
    #     return DataTable(success=False, error="Solicitud inválida")
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
        return custom_datatable_sucess_false(error)
    return paginate(resultados)


@redam.get("/{redam_id}", response_model=OneRedamOut)
@limiter.limit("40/minute")
async def detalle_redam(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    redam_id: int,
):
    """Detalle de un redam a partir de su id"""
    try:
        resultado = get_redam(database=database, redam_id=redam_id)
    except MyAnyError as error:
        return OneRedamOut(success=False, message=str(error))
    return OneRedamOut.model_validate(resultado)


@redam.get("", response_model=CustomPage[ItemRedamOut])
@limiter.limit("40/minute")
async def paginado_redam(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_userdev)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    nombre: str = None,
    expediente: str = None,
):
    """Paginado de Deudores Alimentarios Morosos"""
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
