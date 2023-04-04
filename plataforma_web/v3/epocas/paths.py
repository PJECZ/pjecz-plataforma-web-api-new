"""
Epocas v3, rutas (paths)
"""
from fastapi import APIRouter
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false
from lib.fastapi_pagination_datatable import DataTablePage, datatable_page_success_false

from .crud import get_epocas, get_epoca
from .schemas import EpocaOut, OneEpocaOut

epocas = APIRouter(prefix="/v3/epocas", tags=["tesis jurisprudencias"])


@epocas.get("", response_model=CustomPage[EpocaOut])
async def listado_epocas(db: DatabaseSession):
    """Listado de epocas"""
    try:
        resultados = get_epocas(db=db)
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@epocas.get("/datatable", response_model=DataTablePage[EpocaOut])
async def listado_epocas_datatable(db: DatabaseSession):
    """Listado de epocas para DataTable"""
    try:
        resultados = get_epocas(db=db)
    except MyAnyError as error:
        return datatable_page_success_false(error)
    return paginate(resultados)


@epocas.get("/{epoca_id}", response_model=OneEpocaOut)
async def detalle_epoca(
    db: DatabaseSession,
    epoca_id: int,
):
    """Detalle de una epoca a partir de su id"""
    try:
        epoca = get_epoca(db=db, epoca_id=epoca_id)
    except MyAnyError as error:
        return OneEpocaOut(success=False, message=str(error))
    return OneEpocaOut.from_orm(epoca)
