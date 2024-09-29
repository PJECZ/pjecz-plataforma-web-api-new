"""
Tesis Jurisprudencias v3, rutas (paths)
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
from plataforma_web.v3.tesis_jurisprudencias.crud import get_tesis_jurisprudencia, get_tesis_jurisprudencias
from plataforma_web.v3.tesis_jurisprudencias.schemas import ItemTesisJurisprudenciaOut, OneTesisJurisprudenciaOut

tesis_jurisprudencias = APIRouter(prefix="/v3/tesis_jurisprudencias", tags=["tesis jurisprudencias"])


@tesis_jurisprudencias.get("/datatable", response_model=DataTable[ItemTesisJurisprudenciaOut])
@limiter.limit("40/minute")
async def datatable_tesis_jurisprudencias(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    epoca_id: int = None,
    materia_id: int = None,
    materia_clave: str = None,
):
    """DataTable de tesis jurisprudencias"""
    # draw = request.query_params.get("draw")
    # if draw is None or not draw.isdigit() or int(draw) < 1:
    #     return DataTable(success=False, error="Solicitud inválida")
    try:
        resultados = get_tesis_jurisprudencias(
            database=database,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            epoca_id=epoca_id,
            materia_id=materia_id,
            materia_clave=materia_clave,
        )
    except MyAnyError as error:
        return custom_datatable_sucess_false(error)
    return paginate(resultados)


@tesis_jurisprudencias.get("/{tesis_jurisprudencia_id}", response_model=OneTesisJurisprudenciaOut)
@limiter.limit("40/minute")
async def detalle_tesis_jurisprudencia(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    tesis_jurisprudencia_id: int,
):
    """Detalle de una tesis jurisprudencia a partir de su id"""
    try:
        tesis_jurisprudencia = get_tesis_jurisprudencia(database, tesis_jurisprudencia_id)
    except MyAnyError as error:
        return OneTesisJurisprudenciaOut(success=False, message=str(error))
    return OneTesisJurisprudenciaOut.model_validate(tesis_jurisprudencia)


@tesis_jurisprudencias.get("", response_model=CustomPage[ItemTesisJurisprudenciaOut])
@limiter.limit("40/minute")
async def paginado_tesis_jurisprudencias(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_userdev)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    epoca_id: int = None,
    materia_id: int = None,
    materia_clave: str = None,
):
    """Paginado de tesis jurisprudencias"""
    try:
        resultados = get_tesis_jurisprudencias(
            database=database,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            epoca_id=epoca_id,
            materia_id=materia_id,
            materia_clave=materia_clave,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)
