"""
Autoridades v3, rutas (paths)
"""

from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_username
from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList, custom_list_success_false
from plataforma_web.v3.autoridades.crud import get_autoridad_with_clave, get_autoridades
from plataforma_web.v3.autoridades.schemas import ItemAutoridadOut, OneAutoridadOut

autoridades = APIRouter(prefix="/v3/autoridades", tags=["autoridades"])


@autoridades.get("/{autoridad_clave}", response_model=OneAutoridadOut)
async def detalle_autoridad(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    autoridad_clave: str,
):
    """Detalle de una autoridad a partir de su clave"""
    try:
        autoridad = get_autoridad_with_clave(database, autoridad_clave)
    except MyAnyError as error:
        return OneAutoridadOut(success=False, message=str(error))
    return OneAutoridadOut.model_validate(autoridad)


@autoridades.get("", response_model=CustomList[ItemAutoridadOut])
async def listado_autoridades(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    distrito_id: int = None,
    distrito_clave: str = None,
    es_cemasc: bool = None,
    es_creador_glosas: bool = None,
    es_defensoria: bool = None,
    es_jurisdiccional: bool = None,
    es_notaria: bool = None,
    materia_id: int = None,
    materia_clave: str = None,
):
    """Listado de autoridades"""
    try:
        resultados = get_autoridades(
            database=database,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            es_cemasc=es_cemasc,
            es_creador_glosas=es_creador_glosas,
            es_defensoria=es_defensoria,
            es_jurisdiccional=es_jurisdiccional,
            es_notaria=es_notaria,
            materia_id=materia_id,
            materia_clave=materia_clave,
        )
    except MyAnyError as error:
        return custom_list_success_false(error)
    return paginate(resultados)
