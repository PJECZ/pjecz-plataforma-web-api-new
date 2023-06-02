"""
Materias v3, rutas (paths)
"""
from fastapi import APIRouter
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList, custom_list_success_false
from lib.fastapi_pagination_datatable import DataTablePage, datatable_page_success_false

from .crud import get_materias, get_materia_with_clave
from .schemas import MateriaOut, OneMateriaOut

materias = APIRouter(prefix="/v3/materias", tags=["materias"])


@materias.get("", response_model=CustomList[MateriaOut])
async def listado_materias(
    db: DatabaseSession,
):
    """Listado de materias"""
    try:
        resultados = get_materias(db=db)
    except MyAnyError as error:
        return custom_list_success_false(error)
    return paginate(resultados)


@materias.get("/datatable", response_model=DataTablePage[MateriaOut])
async def listado_materias_datatable(
    db: DatabaseSession,
):
    """Listado de materias para DataTable"""
    try:
        resultados = get_materias(db=db)
    except MyAnyError as error:
        return datatable_page_success_false(error)
    return paginate(resultados)


@materias.get("/{materia_clave}", response_model=OneMateriaOut)
async def detalle_materia(
    db: DatabaseSession,
    materia_clave: str,
):
    """Detalle de una materia a partir de su id"""
    try:
        materia = get_materia_with_clave(db, materia_clave)
    except MyAnyError as error:
        return OneMateriaOut(success=False, message=str(error))
    return OneMateriaOut.from_orm(materia)
