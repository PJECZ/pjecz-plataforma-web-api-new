"""
Distritos v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_user
from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList, custom_list_success_false

from .crud import get_distritos, get_distrito_with_clave
from .schemas import DistritoOut, OneDistritoOut

distritos = APIRouter(prefix="/v3/distritos", tags=["distritos"])


@distritos.get("", response_model=CustomList[DistritoOut])
async def listado_distritos(
    db: DatabaseSession,
    current_user: Annotated[Usuario, Depends(get_current_user)],
    es_distrito_judicial: bool = None,
    es_distrito: bool = None,
    es_jurisdiccional: bool = None,
):
    """Listado de distritos"""
    try:
        resultados = get_distritos(
            db=db,
            es_distrito_judicial=es_distrito_judicial,
            es_distrito=es_distrito,
            es_jurisdiccional=es_jurisdiccional,
        )
    except MyAnyError as error:
        return custom_list_success_false(error)
    return paginate(resultados)


@distritos.get("/{distrito_clave}", response_model=OneDistritoOut)
async def detalle_distrito(
    db: DatabaseSession,
    current_user: Annotated[Usuario, Depends(get_current_user)],
    distrito_clave: str,
):
    """Detalle de un distrito a partir de su clave"""
    try:
        distrito = get_distrito_with_clave(db, distrito_clave)
    except MyAnyError as error:
        return OneDistritoOut(success=False, message=str(error))
    return OneDistritoOut.from_orm(distrito)
