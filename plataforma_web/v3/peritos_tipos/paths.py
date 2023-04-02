"""
Peritos - Tipos v3, rutas (paths)
"""
from fastapi import APIRouter
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false
from lib.fastapi_pagination_datatable import DataTablePage, datatable_page_success_false

from .crud import get_peritos_tipos, get_perito_tipo
from .schemas import PeritoTipoOut, OnePeritoTipoOut

peritos_tipos = APIRouter(prefix="/v3/peritos_tipos", tags=["peritos"])


@peritos_tipos.get("", response_model=CustomPage[PeritoTipoOut])
async def listado_peritos_tipos(
    db: DatabaseSession,
):
    """Listado de tipos de peritos"""
    try:
        resultados = get_peritos_tipos(db=db)
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@peritos_tipos.get("/datatable", response_model=DataTablePage[PeritoTipoOut])
async def listado_peritos_tipos_datatable(
    db: DatabaseSession,
):
    """Listado de tipos de peritos para DataTable"""
    try:
        resultados = get_peritos_tipos(db=db)
    except MyAnyError as error:
        return datatable_page_success_false(error)
    return paginate(resultados)


@peritos_tipos.get("/{perito_tipo_id}", response_model=OnePeritoTipoOut)
async def detalle_perito_tipo(
    db: DatabaseSession,
    perito_tipo_id: int,
):
    """Detalle de un tipo de perito a partir de su id"""
    try:
        perito_tipo = get_perito_tipo(db=db, perito_tipo_id=perito_tipo_id)
    except MyAnyError as error:
        return OnePeritoTipoOut(success=False, message=str(error))
    return OnePeritoTipoOut.from_orm(perito_tipo)
