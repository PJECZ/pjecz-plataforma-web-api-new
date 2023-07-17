"""
Tesis Jurisprudencias v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_user
from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false
from lib.fastapi_pagination_datatable import DataTablePage, datatable_page_success_false

from .crud import get_tesis_jurisprudencia, get_tesis_jurisprudencias
from .schemas import OneTesisJurisprudenciaOut, TesisJurisprudenciaOut

tesis_jurisprudencias = APIRouter(prefix="/v3/tesis_jurisprudencias", tags=["tesis jurisprudencias"])


@tesis_jurisprudencias.get("", response_model=CustomPage[TesisJurisprudenciaOut])
async def listado_tesis_jurisprudencias(
    db: DatabaseSession,
    current_user: Annotated[Usuario, Depends(get_current_user)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    epoca_id: int = None,
    materia_id: int = None,
    materia_clave: str = None,
):
    """Listado de tesis jurisprudencias"""
    try:
        resultados = get_tesis_jurisprudencias(
            db=db,
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


@tesis_jurisprudencias.get("/datatable", response_model=DataTablePage[TesisJurisprudenciaOut])
async def listado_tesis_jurisprudencias_datatable(
    db: DatabaseSession,
    current_user: Annotated[Usuario, Depends(get_current_user)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    epoca_id: int = None,
    materia_id: int = None,
    materia_clave: str = None,
):
    """Listado de tesis jurisprudencias para DataTable"""
    try:
        resultados = get_tesis_jurisprudencias(
            db=db,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            epoca_id=epoca_id,
            materia_id=materia_id,
            materia_clave=materia_clave,
        )
    except MyAnyError as error:
        return datatable_page_success_false(error)
    return paginate(resultados)


@tesis_jurisprudencias.get("/{tesis_jurisprudencia_id}", response_model=OneTesisJurisprudenciaOut)
async def detalle_tesis_jurisprudencia(
    db: DatabaseSession,
    current_user: Annotated[Usuario, Depends(get_current_user)],
    tesis_jurisprudencia_id: int,
):
    """Detalle de una tesis jurisprudencia a partir de su id"""
    try:
        tesis_jurisprudencia = get_tesis_jurisprudencia(db, tesis_jurisprudencia_id)
    except MyAnyError as error:
        return OneTesisJurisprudenciaOut(success=False, message=str(error))
    return OneTesisJurisprudenciaOut.from_orm(tesis_jurisprudencia)
