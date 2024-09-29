"""
Audiencias v3, rutas (paths)
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
from plataforma_web.v3.audiencias.crud import get_audiencia, get_audiencias
from plataforma_web.v3.audiencias.schemas import ItemAudienciaOut, OneAudienciaOut

audiencias = APIRouter(prefix="/v3/audiencias", tags=["audiencias"])


@audiencias.get("/datatable", response_model=DataTable[ItemAudienciaOut])
@limiter.limit("40/minute")
async def datatable_audiencias(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    fecha: date = None,
    fecha_desde: date = None,
    fecha_hasta: date = None,
):
    """DataTable de audiencias"""
    # draw = request.query_params.get("draw")
    # if draw is None or not draw.isdigit() or int(draw) < 1:
    #     return DataTable(success=False, error="Solicitud inválida")
    try:
        resultados = get_audiencias(
            database=database,
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


@audiencias.get("/{audiencia_id}", response_model=OneAudienciaOut)
@limiter.limit("40/minute")
async def detalle_audiencia(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    audiencia_id: int,
):
    """Detalle de un audiencia a partir de su id"""
    try:
        audiencia = get_audiencia(database=database, audiencia_id=audiencia_id)
    except MyAnyError as error:
        return OneAudienciaOut(success=False, message=error)
    return OneAudienciaOut.model_validate(audiencia)


@audiencias.get("", response_model=CustomPage[ItemAudienciaOut])
@limiter.limit("40/minute")
async def paginado_audiencias(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_userdev)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    fecha: date = None,
    fecha_desde: date = None,
    fecha_hasta: date = None,
):
    """Paginado de audiencias"""
    try:
        resultados = get_audiencias(
            database=database,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            fecha=fecha,
            fecha_desde=fecha_desde,
            fecha_hasta=fecha_hasta,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)
