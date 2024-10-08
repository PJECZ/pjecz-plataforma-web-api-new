"""
Abogados v3, rutas (paths)
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
from plataforma_web.v3.abogados.crud import get_abogado, get_abogados
from plataforma_web.v3.abogados.schemas import ItemAbogadoOut, OneAbogadoOut

abogados = APIRouter(prefix="/v3/abogados", tags=["abogados"])


@abogados.get("/datatable", response_model=DataTable[ItemAbogadoOut])
@limiter.limit("40/minute")
async def datatable_abogados(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    nombre: str = None,
    anio_desde: int = None,
    anio_hasta: int = None,
):
    """DataTable de abogados"""
    # draw = request.query_params.get("draw")
    # if draw is None or not draw.isdigit() or int(draw) < 1:
    #     return DataTable(success=False, error="Solicitud inválida")
    try:
        resultados = get_abogados(
            database=database,
            nombre=nombre,
            anio_desde=anio_desde,
            anio_hasta=anio_hasta,
        )
    except MyAnyError as error:
        return custom_datatable_sucess_false(error)
    return paginate(resultados)


@abogados.get("/{abogado_id}", response_model=OneAbogadoOut)
@limiter.limit("40/minute")
async def detalle_abogado(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    abogado_id: int,
):
    """Detalle de un abogado a partir de su id"""
    try:
        abogado = get_abogado(database=database, abogado_id=abogado_id)
    except MyAnyError as error:
        return OneAbogadoOut(success=False, message=str(error))
    return OneAbogadoOut.model_validate(abogado)


@abogados.get("", response_model=CustomPage[ItemAbogadoOut])
@limiter.limit("40/minute")
async def paginado_abogados(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_userdev)],
    nombre: str = None,
    anio_desde: int = None,
    anio_hasta: int = None,
):
    """Paginado de abogados"""
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
