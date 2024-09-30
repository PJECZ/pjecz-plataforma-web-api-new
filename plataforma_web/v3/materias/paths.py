"""
Materias v3, rutas (paths)
"""

from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_username
from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList, custom_list_success_false
from plataforma_web.v3.materias.crud import get_materia_with_clave, get_materias
from plataforma_web.v3.materias.schemas import ItemMateriaOut, OneMateriaOut

materias = APIRouter(prefix="/v3/materias", tags=["materias"])


@materias.get("/{materia_clave}", response_model=OneMateriaOut)
async def detalle_materia(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    materia_clave: str,
):
    """Detalle de una materia a partir de su id"""
    try:
        materia = get_materia_with_clave(database, materia_clave)
    except MyAnyError as error:
        return OneMateriaOut(success=False, message=str(error))
    return OneMateriaOut.model_validate(materia)


@materias.get("", response_model=CustomList[ItemMateriaOut])
async def listado_materias(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    en_sentencias: bool = None,
):
    """Listado de materias"""
    try:
        resultados = get_materias(database, en_sentencias)
    except MyAnyError as error:
        return custom_list_success_false(error)
    return paginate(resultados)
