"""
Listas de Acuerdos v3, rutas (paths)
"""
from datetime import date
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_user
from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false
from lib.fastapi_pagination_datatable import DataTablePage, datatable_page_success_false

from .crud import get_listas_de_acuerdos, get_lista_de_acuerdo
from .schemas import ListaDeAcuerdoOut, OneListaDeAcuerdoOut

listas_de_acuerdos = APIRouter(prefix="/v3/listas_de_acuerdos", tags=["listas de acuerdos"])


@listas_de_acuerdos.get("", response_model=CustomPage[ListaDeAcuerdoOut])
async def listado_listas_de_acuerdos(
    db: DatabaseSession,
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
            db=db,
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


@listas_de_acuerdos.get("/datatable", response_model=DataTablePage[ListaDeAcuerdoOut])
async def listado_listas_de_acuerdos_datatable(
    db: DatabaseSession,
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
    try:
        resultados = get_listas_de_acuerdos(
            db=db,
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


@listas_de_acuerdos.get("/{lista_de_acuerdo_id}", response_model=OneListaDeAcuerdoOut)
async def detalle_lista_de_acuerdo(
    db: DatabaseSession,
    current_user: Annotated[Usuario, Depends(get_current_user)],
    lista_de_acuerdo_id: int,
):
    """Detalle de una lista de acuerdo a partir de su id"""
    try:
        lista_de_acuerdo = get_lista_de_acuerdo(db, lista_de_acuerdo_id)
    except MyAnyError as error:
        return OneListaDeAcuerdoOut(success=False, message=str(error))
    return OneListaDeAcuerdoOut.from_orm(lista_de_acuerdo)
