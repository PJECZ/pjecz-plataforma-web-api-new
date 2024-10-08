"""
Peritos v3, rutas (paths)
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
from plataforma_web.v3.peritos.crud import get_perito, get_peritos
from plataforma_web.v3.peritos.schemas import ItemPeritoOut, OnePeritoOut

peritos = APIRouter(prefix="/v3/peritos", tags=["peritos"])


@peritos.get("/datatable", response_model=DataTable[ItemPeritoOut])
@limiter.limit("40/minute")
async def listado_peritos_datatable(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    distrito_id: int = None,
    distrito_clave: str = None,
    nombre: str = None,
    perito_tipo_id: int = None,
):
    """DataTable de peritos"""
    # draw = request.query_params.get("draw")
    # if draw is None or not draw.isdigit() or int(draw) < 1:
    #     return DataTable(success=False, error="Solicitud inválida")
    try:
        resultados = get_peritos(
            database=database,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            nombre=nombre,
            perito_tipo_id=perito_tipo_id,
        )
    except MyAnyError as error:
        return custom_datatable_sucess_false(error)
    return paginate(resultados)


@peritos.get("/{perito_id}", response_model=OnePeritoOut)
@limiter.limit("40/minute")
async def detalle_perito(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    perito_id: int,
):
    """Detalle de un perito a partir de su id"""
    try:
        perito = get_perito(database=database, perito_id=perito_id)
    except MyAnyError as error:
        return OnePeritoOut(success=False, message=str(error))
    return OnePeritoOut.model_validate(perito)


@peritos.get("", response_model=CustomPage[ItemPeritoOut])
@limiter.limit("40/minute")
async def paginado_peritos(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_userdev)],
    distrito_id: int = None,
    distrito_clave: str = None,
    nombre: str = None,
    perito_tipo_id: int = None,
):
    """Paginado de peritos"""
    try:
        resultados = get_peritos(
            database=database,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            nombre=nombre,
            perito_tipo_id=perito_tipo_id,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)
