"""
Materias v3, rutas (paths)
"""
from fastapi import APIRouter
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from .crud import get_materias, get_materia
from .schemas import MateriaOut, OneMateriaOut

materias = APIRouter(prefix="/v3/materias", tags=["autoridades"])


@materias.get("", response_model=CustomPage[MateriaOut])
async def listado_materias(
    db: DatabaseSession,
):
    """Listado de materias"""
    try:
        resultados = get_materias(db=db)
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@materias.get("/{materia_id}", response_model=OneMateriaOut)
async def detalle_materia(
    db: DatabaseSession,
    materia_id: int,
):
    """Detalle de una materia a partir de su id"""
    try:
        materia = get_materia(db=db, materia_id=materia_id)
    except MyAnyError as error:
        return OneMateriaOut(success=False, message=str(error))
    return OneMateriaOut.from_orm(materia)
