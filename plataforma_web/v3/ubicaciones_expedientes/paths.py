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
from lib.fastapi_pagination_datatable import DataTable, custom_datatable_sucess_false
from lib.limiter import limiter

from .crud import get_ubicacion_expediente, get_ubicaciones_expedientes
from .schemas import OneUbicacionExpedienteOut, UbicacionExpedienteOut

ubicaciones_expedientes = APIRouter(prefix="/v3/ubicaciones_expedientes", tags=["ubicaciones de expedientes"])


@ubicaciones_expedientes.get("/datatable", response_model=DataTable[UbicacionExpedienteOut])
@limiter.limit("40/minute")
async def datatable_ubicaciones_expedientes(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    expediente: str = None,
):
    """DataTable de ubicaciones de expedientes"""
    # draw = request.query_params.get("draw")
    # if draw is None or not draw.isdigit() or int(draw) < 1:
    #     return DataTable(success=False, error="Solicitud inválida")
    try:
        resultados = get_ubicaciones_expedientes(
            database=database,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            expediente=expediente,
        )
    except MyAnyError as error:
        return custom_datatable_sucess_false(error)
    return paginate(resultados)


@ubicaciones_expedientes.get("/{ubicacion_expediente_id}", response_model=OneUbicacionExpedienteOut)
@limiter.limit("40/minute")
async def detalle_ubicacion_expediente(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    ubicacion_expediente_id: int,
):
    """Detalle de un ubicacion_expediente a partir de su id"""
    try:
        ubicacion_expediente = get_ubicacion_expediente(database=database, ubicacion_expediente_id=ubicacion_expediente_id)
    except MyAnyError as error:
        return OneUbicacionExpedienteOut(success=False, message=str(error))
    return OneUbicacionExpedienteOut.model_validate(ubicacion_expediente)


@ubicaciones_expedientes.get("", response_model=CustomPage[UbicacionExpedienteOut])
@limiter.limit("40/minute")
async def listado_ubicaciones_expedientes(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_userdev)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    expediente: str = None,
):
    """Paginado de ubicaciones de expedientes"""
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
