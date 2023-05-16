"""
Autoridades v3, rutas (paths)
"""
from fastapi import APIRouter
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false
from lib.fastapi_pagination_datatable import DataTablePage, datatable_page_success_false

from .crud import get_autoridades, get_autoridad_with_clave
from .schemas import AutoridadOut, OneAutoridadOut

autoridades = APIRouter(prefix="/v3/autoridades", tags=["autoridades"])


@autoridades.get("", response_model=CustomPage[AutoridadOut])
async def listado_autoridades(
    db: DatabaseSession,
    distrito_id: int = None,
    distrito_clave: str = None,
    es_cemasc: bool = None,
    es_creador_glosas: bool = None,
    es_defensoria: bool = None,
    es_jurisdiccional: bool = None,
    es_notaria: bool = None,
):
    """Listado de autoridades"""
    try:
        resultados = get_autoridades(
            db=db,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            es_cemasc=es_cemasc,
            es_creador_glosas=es_creador_glosas,
            es_defensoria=es_defensoria,
            es_jurisdiccional=es_jurisdiccional,
            es_notaria=es_notaria,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@autoridades.get("/datatable", response_model=DataTablePage[AutoridadOut])
async def listado_autoridades_datatable(
    db: DatabaseSession,
    distrito_id: int = None,
    distrito_clave: str = None,
    es_cemasc: bool = None,
    es_creador_glosas: bool = None,
    es_defensoria: bool = None,
    es_jurisdiccional: bool = None,
    es_notaria: bool = None,
):
    """Listado de autoridades para DataTable"""
    try:
        resultados = get_autoridades(
            db=db,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            es_cemasc=es_cemasc,
            es_creador_glosas=es_creador_glosas,
            es_defensoria=es_defensoria,
            es_jurisdiccional=es_jurisdiccional,
            es_notaria=es_notaria,
        )
    except MyAnyError as error:
        return datatable_page_success_false(error)
    return paginate(resultados)


@autoridades.get("/{clave}", response_model=OneAutoridadOut)
async def detalle_autoridad(
    db: DatabaseSession,
    clave: str,
):
    """Detalle de una autoridad a partir de su clave"""
    try:
        autoridad = get_autoridad_with_clave(db=db, clave=clave)
    except MyAnyError as error:
        return OneAutoridadOut(success=False, message=str(error))
    return OneAutoridadOut.from_orm(autoridad)
