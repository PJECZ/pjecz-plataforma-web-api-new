"""
Abogados v3, rutas (paths)
"""
from fastapi import APIRouter
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false
from lib.fastapi_pagination_datatable import DataTablePage, datatable_page_success_false

from .crud import get_abogados, get_abogado
from .schemas import AbogadoOut, OneAbogadoOut

abogados = APIRouter(prefix="/v3/abogados", tags=["abogados"])


@abogados.get("", response_model=CustomPage[AbogadoOut])
async def listado_abogados(
    db: DatabaseSession,
    nombre: str = None,
    anio_desde: int = None,
    anio_hasta: int = None,
):
    """Listado de abogados"""
    try:
        resultados = get_abogados(
            db=db,
            nombre=nombre,
            anio_desde=anio_desde,
            anio_hasta=anio_hasta,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@abogados.get("/datatable", response_model=DataTablePage[AbogadoOut])
async def listado_abogados_datatable(
    db: DatabaseSession,
    nombre: str = None,
    anio_desde: int = None,
    anio_hasta: int = None,
):
    """Listado de abogados para DataTable"""
    try:
        resultados = get_abogados(
            db=db,
            nombre=nombre,
            anio_desde=anio_desde,
            anio_hasta=anio_hasta,
        )
    except MyAnyError as error:
        return datatable_page_success_false(error)
    return paginate(resultados)


@abogados.get("/{abogado_id}", response_model=OneAbogadoOut)
async def detalle_abogado(
    db: DatabaseSession,
    abogado_id: int,
):
    """Detalle de un abogado a partir de su id"""
    try:
        abogado = get_abogado(db=db, abogado_id=abogado_id)
    except MyAnyError as error:
        return OneAbogadoOut(success=False, message=str(error))
    return OneAbogadoOut.from_orm(abogado)
