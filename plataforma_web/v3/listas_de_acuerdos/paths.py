"""
Listas de Acuerdos v3, rutas (paths)
"""

from datetime import date
from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_userdev, get_current_username
from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false
from lib.fastapi_pagination_datatable import DataTable, custom_datatable_sucess_false
from lib.limiter import limiter

from .crud import get_lista_de_acuerdo, get_listas_de_acuerdos
from .schemas import ListaDeAcuerdoOut, OneListaDeAcuerdoOut

listas_de_acuerdos = APIRouter(prefix="/v3/listas_de_acuerdos", tags=["listas de acuerdos"])


@listas_de_acuerdos.get("/datatable", response_model=DataTable[ListaDeAcuerdoOut])
@limiter.limit("40/minute")
async def datatable_listas_de_acuerdos(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    anio: int = None,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    fecha: date = None,
    fecha_desde: date = None,
    fecha_hasta: date = None,
):
    """DataTable de listas de acuerdos"""
    # draw = request.query_params.get("draw")
    # if draw is None or not draw.isdigit() or int(draw) < 1:
    #     return DataTable(success=False, error="Solicitud inválida")
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
        return custom_datatable_sucess_false(error)
    return paginate(resultados)


@listas_de_acuerdos.get("/paginado", response_model=CustomPage[ListaDeAcuerdoOut])
@limiter.limit("40/minute")
async def paginado_listas_de_acuerdos(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_userdev)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    anio: int = None,
    fecha: date = None,
    fecha_desde: date = None,
    fecha_hasta: date = None,
):
    """Paginado de listas de acuerdos"""
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
@limiter.limit("40/minute")
async def detalle_lista_de_acuerdo(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    lista_de_acuerdo_id: int,
):
    """Detalle de un lista_de_acuerdo a partir de su id"""
    try:
        lista_de_acuerdo = get_lista_de_acuerdo(database=database, lista_de_acuerdo_id=lista_de_acuerdo_id)
    except MyAnyError as error:
        return OneListaDeAcuerdoOut(success=False, message=str(error))
    return OneListaDeAcuerdoOut.model_validate(lista_de_acuerdo)
