"""
Abogados v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_user
from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false
from lib.fastapi_pagination_datatable import DataTablePage, datatable_page_success_false

from .crud import get_abogados
from .schemas import AbogadoOut

abogados = APIRouter(prefix="/v3/abogados", tags=["abogados"])


@abogados.get("", response_model=CustomPage[AbogadoOut])
async def listado_abogados(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_user)],
    nombre: str = None,
    anio_desde: int = None,
    anio_hasta: int = None,
):
    """Listado de abogados"""
    try:
        resultados = get_abogados(
            database=database,
            nombre=nombre,
            anio_desde=anio_desde,
            anio_hasta=anio_hasta,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@abogados.get("/datatable", response_model=DataTablePage[AbogadoOut])
async def listado_abogados_datatable(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_user)],
    nombre: str = None,
    anio_desde: int = None,
    anio_hasta: int = None,
):
    """Listado de abogados para DataTable"""
    try:
        resultados = get_abogados(
            database=database,
            nombre=nombre,
            anio_desde=anio_desde,
            anio_hasta=anio_hasta,
        )
    except MyAnyError as error:
        return datatable_page_success_false(error)
    return paginate(resultados)
