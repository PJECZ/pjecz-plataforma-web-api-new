"""
Distritos v3, rutas (paths)
"""
from fastapi import APIRouter
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from .crud import get_distritos, get_distrito_with_clave
from .schemas import DistritoOut, OneDistritoOut

distritos = APIRouter(prefix="/v3/distritos", tags=["autoridades"])


@distritos.get("", response_model=CustomPage[DistritoOut])
async def listado_distritos(
    db: DatabaseSession,
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
        return custom_page_success_false(error)
    return paginate(resultados)


@distritos.get("/{clave}", response_model=OneDistritoOut)
async def detalle_distrito(
    clave: str,
    db: DatabaseSession,
):
    """Detalle de un distrito a partir de su clave"""
    try:
        distrito = get_distrito_with_clave(db=db, clave=clave)
    except MyAnyError as error:
        return OneDistritoOut(success=False, message=str(error))
    return OneDistritoOut.from_orm(distrito)
