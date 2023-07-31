"""
Peritos - Tipos v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_user
from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList, custom_list_success_false

from .crud import get_perito_tipo, get_peritos_tipos
from .schemas import OnePeritoTipoOut, PeritoTipoOut

peritos_tipos = APIRouter(prefix="/v3/peritos_tipos", tags=["peritos"])


@peritos_tipos.get("", response_model=CustomList[PeritoTipoOut])
async def listado_peritos_tipos(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_user)],
):
    """Listado de tipos de peritos"""
    try:
        resultados = get_peritos_tipos(database=database)
    except MyAnyError as error:
        return custom_list_success_false(error)
    return paginate(resultados)


@peritos_tipos.get("/{perito_tipo_id}", response_model=OnePeritoTipoOut)
async def detalle_perito_tipo(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_user)],
    perito_tipo_id: int,
):
    """Detalle de un tipo de perito a partir de su id"""
    try:
        perito_tipo = get_perito_tipo(database, perito_tipo_id)
    except MyAnyError as error:
        return OnePeritoTipoOut(success=False, message=str(error))
    return OnePeritoTipoOut.from_orm(perito_tipo)
