"""
Glosas v3, rutas (paths)
"""
from datetime import date
from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_userdev, get_current_username
from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false
from lib.fastapi_pagination_datatable import DataTablePage, datatable_page_success_false

from .crud import get_glosa, get_glosas
from .schemas import GlosaOut, OneGlosaOut

glosas = APIRouter(prefix="/v3/glosas", tags=["glosas"])


@glosas.get("/datatable", response_model=DataTablePage[GlosaOut])
async def listado_glosas_datatable(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    expediente: str = None,
    anio: int = None,
    fecha: date = None,
    fecha_desde: date = None,
    fecha_hasta: date = None,
):
    """Listado de glosas para DataTable"""
    draw = request.query_params.get("draw")
    if draw is None or not draw.isdigit() or int(draw) < 1:
        return datatable_page_success_false("Invalid request")
    try:
        resultados = get_glosas(
            database=database,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            expediente=expediente,
            anio=anio,
            fecha=fecha,
            fecha_desde=fecha_desde,
            fecha_hasta=fecha_hasta,
        )
    except MyAnyError as error:
        return datatable_page_success_false(error)
    return paginate(resultados)


@glosas.get("/paginado", response_model=CustomPage[GlosaOut])
async def listado_glosas(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_userdev)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    expediente: str = None,
    anio: int = None,
    fecha: date = None,
    fecha_desde: date = None,
    fecha_hasta: date = None,
):
    """Listado de glosas"""
    try:
        resultados = get_glosas(
            database=database,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            expediente=expediente,
            anio=anio,
            fecha=fecha,
            fecha_desde=fecha_desde,
            fecha_hasta=fecha_hasta,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@glosas.get("/{glosa_id}", response_model=OneGlosaOut)
async def detalle_glosa(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    glosa_id: int,
):
    """Detalle de un glosa a partir de su id"""
    try:
        glosa = get_glosa(database=database, glosa_id=glosa_id)
    except MyAnyError as error:
        return OneGlosaOut(success=False, error=error)
    return OneGlosaOut.from_orm(glosa)
