"""
Ubicaciones de Expedientes v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_userdev, get_current_username
from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false
from lib.fastapi_pagination_datatable import DataTablePage, datatable_page_success_false

from .crud import get_ubicacion_expediente, get_ubicaciones_expedientes
from .schemas import OneUbicacionExpedienteOut, UbicacionExpedienteOut

ubicaciones_expedientes = APIRouter(prefix="/v3/ubicaciones_expedientes", tags=["ubicaciones de expedientes"])


@ubicaciones_expedientes.get("/datatable", response_model=DataTablePage[UbicacionExpedienteOut])
async def listado_ubicaciones_expedientes_datatable(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    expediente: str = None,
):
    """Listado de ubicaciones de expedientes para DataTable"""
    draw = request.query_params.get("draw")
    if draw is None or not draw.isdigit() or int(draw) < 1:
        return datatable_page_success_false("Invalid request")
    try:
        resultados = get_ubicaciones_expedientes(
            database=database,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            expediente=expediente,
        )
    except MyAnyError as error:
        return datatable_page_success_false(error)
    return paginate(resultados)


@ubicaciones_expedientes.get("/paginado", response_model=CustomPage[UbicacionExpedienteOut])
async def listado_ubicaciones_expedientes(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_userdev)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    expediente: str = None,
):
    """Listado de ubicaciones de expedientes"""
    try:
        resultados = get_ubicaciones_expedientes(
            database=database,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            expediente=expediente,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@ubicaciones_expedientes.get("/{ubicacion_expediente_id}", response_model=OneUbicacionExpedienteOut)
async def detalle_ubicacion_expediente(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    ubicacion_expediente_id: int,
):
    """Detalle de un ubicacion_expediente a partir de su id"""
    try:
        ubicacion_expediente = get_ubicacion_expediente(database=database, ubicacion_expediente_id=ubicacion_expediente_id)
    except MyAnyError as error:
        return OneUbicacionExpedienteOut(success=False, error=error)
    return OneUbicacionExpedienteOut.from_orm(ubicacion_expediente)
