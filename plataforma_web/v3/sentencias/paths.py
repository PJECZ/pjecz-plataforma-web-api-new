"""
Sentencias v3, rutas (paths)
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

from .crud import get_sentencia, get_sentencias
from .schemas import OneSentenciaOut, SentenciaOut

sentencias = APIRouter(prefix="/v3/sentencias", tags=["sentencias"])


@sentencias.get("/datatable", response_model=DataTablePage[SentenciaOut])
async def listado_sentencias_datatable(
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
    materia_tipo_juicio_id: int = None,
    sentencia: str = None,
):
    """Listado de sentencias para DataTable"""
    draw = request.query_params.get("draw")
    if not draw.isdigit() or int(draw) < 1:
        return datatable_page_success_false("Invalid request")
    try:
        resultados = get_sentencias(
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
            materia_tipo_juicio_id=materia_tipo_juicio_id,
            sentencia=sentencia,
        )
    except MyAnyError as error:
        return datatable_page_success_false(error)
    return paginate(resultados)


@sentencias.get("/paginado", response_model=CustomPage[SentenciaOut])
async def listado_sentencias(
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
    materia_tipo_juicio_id: int = None,
    sentencia: str = None,
):
    """Listado de sentencias"""
    try:
        resultados = get_sentencias(
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
            materia_tipo_juicio_id=materia_tipo_juicio_id,
            sentencia=sentencia,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@sentencias.get("/{sentencia_id}", response_model=OneSentenciaOut)
async def detalle_sentencia(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_user)],
    sentencia_id: int,
):
    """Detalle de un sentencia a partir de su id"""
    try:
        sentencia = get_sentencia(database=database, sentencia_id=sentencia_id)
    except MyAnyError as error:
        return OneSentenciaOut(success=False, error=error)
    return OneSentenciaOut.model_validate(sentencia)
