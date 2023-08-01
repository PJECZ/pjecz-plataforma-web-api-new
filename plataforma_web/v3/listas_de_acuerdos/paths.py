"""
Listas de Acuerdos v3, rutas (paths)
"""
from datetime import date
from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_user
from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false
from lib.fastapi_pagination_datatable import DataTablePage, datatable_page_success_false

from .crud import get_lista_de_acuerdo, get_listas_de_acuerdos
from .schemas import ListaDeAcuerdoOut, OneListaDeAcuerdoOut

listas_de_acuerdos = APIRouter(prefix="/v3/listas_de_acuerdos", tags=["listas de acuerdos"])


@listas_de_acuerdos.get("/datatable", response_model=DataTablePage[ListaDeAcuerdoOut])
async def listado_listas_de_acuerdos_datatable(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_user)],
    anio: int = None,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    fecha: date = None,
    fecha_desde: date = None,
    fecha_hasta: date = None,
):
    """Listado de listas de acuerdos para DataTable"""
    draw = request.query_params.get("draw")
    if not draw.isdigit() or int(draw) < 1:
        return datatable_page_success_false("Invalid request")
    try:
        resultados = get_listas_de_acuerdos(
            database=database,
            anio=anio,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            fecha=fecha,
            fecha_desde=fecha_desde,
            fecha_hasta=fecha_hasta,
        )
    except MyAnyError as error:
        return datatable_page_success_false(error)
    return paginate(resultados)


@listas_de_acuerdos.get("/paginado", response_model=CustomPage[ListaDeAcuerdoOut])
async def listado_listas_de_acuerdos(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_user)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    anio: int = None,
    fecha: date = None,
    fecha_desde: date = None,
    fecha_hasta: date = None,
):
    """Listado de listas de acuerdos"""
    try:
        resultados = get_listas_de_acuerdos(
            database=database,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            anio=anio,
            fecha=fecha,
            fecha_desde=fecha_desde,
            fecha_hasta=fecha_hasta,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@listas_de_acuerdos.get("/{lista_de_acuerdo_id}", response_model=OneListaDeAcuerdoOut)
async def detalle_lista_de_acuerdo(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_user)],
    lista_de_acuerdo_id: int,
):
    """Detalle de un lista_de_acuerdo a partir de su id"""
    try:
        lista_de_acuerdo = get_lista_de_acuerdo(database=database, lista_de_acuerdo_id=lista_de_acuerdo_id)
    except MyAnyError as error:
        return OneListaDeAcuerdoOut(success=False, error=error)
    return OneListaDeAcuerdoOut.model_validate(lista_de_acuerdo)
