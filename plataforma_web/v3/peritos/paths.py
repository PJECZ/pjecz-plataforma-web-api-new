"""
Peritos v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_user
from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false
from lib.fastapi_pagination_datatable import DataTablePage, datatable_page_success_false

from .crud import get_perito, get_peritos
from .schemas import OnePeritoOut, PeritoOut

peritos = APIRouter(prefix="/v3/peritos", tags=["peritos"])


@peritos.get("/datatable", response_model=DataTablePage[PeritoOut])
async def listado_peritos_datatable(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_user)],
    distrito_id: int = None,
    distrito_clave: str = None,
    nombre: str = None,
    perito_tipo_id: int = None,
):
    """Listado de peritos para DataTable"""
    draw = request.query_params.get("draw")
    if draw is None or not draw.isdigit() or int(draw) < 1:
        return datatable_page_success_false("Invalid request")
    try:
        resultados = get_peritos(
            database=database,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            nombre=nombre,
            perito_tipo_id=perito_tipo_id,
        )
    except MyAnyError as error:
        return datatable_page_success_false(error)
    return paginate(resultados)


@peritos.get("/paginado", response_model=CustomPage[PeritoOut])
async def listado_peritos(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_user)],
    distrito_id: int = None,
    distrito_clave: str = None,
    nombre: str = None,
    perito_tipo_id: int = None,
):
    """Listado de peritos"""
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


@peritos.get("/{perito_id}", response_model=OnePeritoOut)
async def detalle_perito(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_user)],
    perito_id: int,
):
    """Detalle de un perito a partir de su id"""
    try:
        perito = get_perito(database=database, perito_id=perito_id)
    except MyAnyError as error:
        return OnePeritoOut(success=False, error=error)
    return OnePeritoOut.from_orm(perito)
