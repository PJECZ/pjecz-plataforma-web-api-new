"""
Sentencias v3, rutas (paths)
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
from plataforma_web.v3.sentencias.crud import get_sentencia, get_sentencias
from plataforma_web.v3.sentencias.schemas import ItemSentenciaOut, OneSentenciaOut

sentencias = APIRouter(prefix="/v3/sentencias", tags=["sentencias"])


@sentencias.get("/datatable", response_model=DataTable[ItemSentenciaOut])
@limiter.limit("40/minute")
async def listado_sentencias_datatable(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
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
    """DataTable de sentencias"""
    # draw = request.query_params.get("draw")
    # if draw is None or not draw.isdigit() or int(draw) < 1:
    #     return DataTable(success=False, error="Solicitud inválida")
    try:
        resultados = get_sentencias(
            database=database,
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
        return custom_datatable_sucess_false(error)
    return paginate(resultados)


@sentencias.get("/{sentencia_id}", response_model=OneSentenciaOut)
@limiter.limit("40/minute")
async def detalle_sentencia(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    sentencia_id: int,
):
    """Detalle de un sentencia a partir de su id"""
    try:
        sentencia = get_sentencia(database=database, sentencia_id=sentencia_id)
    except MyAnyError as error:
        return OneSentenciaOut(success=False, message=str(error))
    return OneSentenciaOut.model_validate(sentencia)


@sentencias.get("", response_model=CustomPage[ItemSentenciaOut])
@limiter.limit("40/minute")
async def paginado_sentencias(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_userdev)],
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
    """Paginado de sentencias"""
    try:
        resultados = get_sentencias(
            database=database,
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
