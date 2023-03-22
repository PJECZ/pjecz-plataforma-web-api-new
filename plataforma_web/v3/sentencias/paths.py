"""
Sentencias v3, rutas (paths)
"""
from datetime import date

from fastapi import APIRouter
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from .crud import get_sentencias, get_sentencia
from .schemas import SentenciaOut, OneSentenciaOut

sentencias = APIRouter(prefix="/v3/sentencias", tags=["categoria"])


@sentencias.get("", response_model=CustomPage[SentenciaOut])
async def listado_sentencias(
    db: DatabaseSession,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    anio: int = None,
    fecha: date = None,
):
    """Listado de sentencias"""
    try:
        resultados = get_sentencias(
            db=db,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            anio=anio,
            fecha=fecha,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@sentencias.get("/{sentencia_id}", response_model=OneSentenciaOut)
async def detalle_sentencia(
    sentencia_id: int,
    db: DatabaseSession,
):
    """Detalle de una sentencia a partir de su id"""
    try:
        sentencia = get_sentencia(db=db, sentencia_id=sentencia_id)
    except MyAnyError as error:
        return OneSentenciaOut(success=False, message=str(error))
    return OneSentenciaOut.from_orm(sentencia)
