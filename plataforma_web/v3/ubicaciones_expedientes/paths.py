"""
Ubicaciones de Expedientes v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_user
from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false
from lib.fastapi_pagination_datatable import DataTablePage, datatable_page_success_false

from .crud import get_ubicaciones_expedientes, get_ubicacion_expediente
from .schemas import UbicacionExpedienteOut, OneUbicacionExpedienteOut

ubicaciones_expedientes = APIRouter(prefix="/v3/ubicaciones_expedientes", tags=["ubicaciones de expedientes"])


@ubicaciones_expedientes.get("", response_model=CustomPage[UbicacionExpedienteOut])
async def listado_ubicaciones_expedientes(
    db: DatabaseSession,
    current_user: Annotated[Usuario, Depends(get_current_user)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    expediente: str = None,
):
    """Listado de ubicaciones de expedientes"""
    try:
        resultados = get_ubicaciones_expedientes(
            db=db,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            expediente=expediente,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@ubicaciones_expedientes.get("/datatable", response_model=DataTablePage[UbicacionExpedienteOut])
async def listado_ubicaciones_expedientes_datatable(
    db: DatabaseSession,
    current_user: Annotated[Usuario, Depends(get_current_user)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    expediente: str = None,
):
    """Listado de ubicaciones de expedientes para DataTable"""
    try:
        resultados = get_ubicaciones_expedientes(
            db=db,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            expediente=expediente,
        )
    except MyAnyError as error:
        return datatable_page_success_false(error)
    return paginate(resultados)


@ubicaciones_expedientes.get("/{ubicacion_expediente_id}", response_model=OneUbicacionExpedienteOut)
async def detalle_ubicacion_expediente(
    db: DatabaseSession,
    current_user: Annotated[Usuario, Depends(get_current_user)],
    ubicacion_expediente_id: int,
):
    """Detalle de una ubicacion de expediente a partir de su id"""
    try:
        ubicacion_expediente = get_ubicacion_expediente(db, ubicacion_expediente_id)
    except MyAnyError as error:
        return OneUbicacionExpedienteOut(success=False, message=str(error))
    return OneUbicacionExpedienteOut.from_orm(ubicacion_expediente)
