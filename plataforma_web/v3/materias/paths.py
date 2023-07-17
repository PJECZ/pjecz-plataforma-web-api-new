"""
Materias v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_user
from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList, custom_list_success_false

from .crud import get_materia_with_clave, get_materias
from .schemas import MateriaOut, OneMateriaOut

materias = APIRouter(prefix="/v3/materias", tags=["materias"])


@materias.get("", response_model=CustomList[MateriaOut])
async def listado_materias(
    db: DatabaseSession,
    current_user: Annotated[Usuario, Depends(get_current_user)],
):
    """Listado de materias"""
    try:
        resultados = get_materias(db=db)
    except MyAnyError as error:
        return custom_list_success_false(error)
    return paginate(resultados)


@materias.get("/{materia_clave}", response_model=OneMateriaOut)
async def detalle_materia(
    db: DatabaseSession,
    current_user: Annotated[Usuario, Depends(get_current_user)],
    materia_clave: str,
):
    """Detalle de una materia a partir de su id"""
    try:
        materia = get_materia_with_clave(db, materia_clave)
    except MyAnyError as error:
        return OneMateriaOut(success=False, message=str(error))
    return OneMateriaOut.from_orm(materia)
