"""
REVSPM Agresores v3, rutas (paths)
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

from .crud import get_repsvm_agresor, get_repsvm_agresores
from .schemas import OneRepsvmAgresorOut, RepsvmAgresorOut

repsvm_agresores = APIRouter(prefix="/v3/repsvm_agresores", tags=["repsvm agresores"])


@repsvm_agresores.get("/datatable", response_model=DataTable[RepsvmAgresorOut])
@limiter.limit("40/minute")
async def listado_repsvm_agresores_datatable(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    distrito_id: int = None,
    distrito_clave: str = None,
    nombre: str = None,
):
    """DataTable de agresores"""
    # draw = request.query_params.get("draw")
    # if draw is None or not draw.isdigit() or int(draw) < 1:
    #     return DataTable(success=False, error="Solicitud inválida")
    try:
        resultados = get_repsvm_agresores(
            database=database,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            nombre=nombre,
        )
    except MyAnyError as error:
        return custom_datatable_sucess_false(error)
    return paginate(resultados)


@repsvm_agresores.get("/paginado", response_model=CustomPage[RepsvmAgresorOut])
@limiter.limit("40/minute")
async def listado_repsvm_agresores(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_userdev)],
    distrito_id: int = None,
    distrito_clave: str = None,
    nombre: str = None,
):
    """Paginado de agresores"""
    try:
        resultados = get_repsvm_agresores(
            database=database,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            nombre=nombre,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@repsvm_agresores.get("/{repsvm_agresor_id}", response_model=OneRepsvmAgresorOut)
@limiter.limit("40/minute")
async def detalle_repsvm_agresor(
    request: Request,
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    repsvm_agresor_id: int,
):
    """Detalle de un agresor a partir de su id"""
    try:
        repsvm_agresor = get_repsvm_agresor(database=database, repsvm_agresor_id=repsvm_agresor_id)
    except MyAnyError as error:
        return OneRepsvmAgresorOut(success=False, message=str(error))
    return OneRepsvmAgresorOut.model_validate(repsvm_agresor)
