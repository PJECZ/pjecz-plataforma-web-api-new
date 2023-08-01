"""
Edictos v3, rutas (paths)
"""
from datetime import date
from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_user
from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false
from lib.fastapi_pagination_datatable import DataTablePage, datatable_page_success_false

from .crud import get_edicto, get_edictos
from .schemas import EdictoOut, OneEdictoOut

edictos = APIRouter(prefix="/v3/edictos", tags=["edictos"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@edictos.get("/datatable", response_model=DataTablePage[EdictoOut])
async def listado_edictos_datatable(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_user)],
    anio: int = None,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    expediente: str = None,
    fecha: date = None,
    fecha_desde: date = None,
    fecha_hasta: date = None,
):
    """Listado de edictos para DataTable"""
    draw = request.query_params.get("draw")
    if draw is None or not draw.isdigit() or int(draw) < 1:
        return datatable_page_success_false("Invalid request")
    try:
        resultados = get_edictos(
            database=database,
            anio=anio,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            expediente=expediente,
            fecha=fecha,
            fecha_desde=fecha_desde,
            fecha_hasta=fecha_hasta,
        )
    except MyAnyError as error:
        return datatable_page_success_false(error)
    return paginate(resultados)


@edictos.get("/paginado", response_model=CustomPage[EdictoOut])
async def listado_edictos(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_user)],
    anio: int = None,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    expediente: str = None,
    fecha: date = None,
    fecha_desde: date = None,
    fecha_hasta: date = None,
):
    """Listado de edictos"""
    try:
        resultados = get_edictos(
            database=database,
            anio=anio,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            expediente=expediente,
            fecha=fecha,
            fecha_desde=fecha_desde,
            fecha_hasta=fecha_hasta,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@edictos.get("/{edicto_id}", response_model=OneEdictoOut)
async def detalle_edicto(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_user)],
    edicto_id: int,
):
    """Detalle de un edicto a partir de su id"""
    try:
        edicto = get_edicto(database=database, edicto_id=edicto_id)
    except MyAnyError as error:
        return OneEdictoOut(success=False, error=error)
    return OneEdictoOut.from_orm(edicto)
