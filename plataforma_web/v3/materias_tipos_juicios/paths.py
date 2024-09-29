"""
Materias-Tipos de Juicios v3, rutas (paths)
"""

from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_username
from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList, custom_list_success_false

from .crud import get_materia_tipo_juicio, get_materias_tipos_juicios
from .schemas import MateriaTipoJuicioOut, OneMateriaTipoJuicioOut

materias_tipos_juicios = APIRouter(prefix="/v3/materias_tipos_juicios", tags=["sentencias"])


@materias_tipos_juicios.get("/{materia_tipo_juicio_id}", response_model=OneMateriaTipoJuicioOut)
async def detalle_materia_tipo_juicio(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    materia_tipo_juicio_id: int,
):
    """Detalle de una materia-tipo de juicio a partir de su id"""
    try:
        materia_tipo_juicio = get_materia_tipo_juicio(database, materia_tipo_juicio_id)
    except MyAnyError as error:
        return OneMateriaTipoJuicioOut(success=False, message=str(error))
    return OneMateriaTipoJuicioOut.model_validate(materia_tipo_juicio)


@materias_tipos_juicios.get("", response_model=CustomList[MateriaTipoJuicioOut])
async def listado_materias_tipos_juicios(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    materia_id: int = None,
    materia_clave: str = None,
):
    """Listado de materias-tipos de juicios"""
    try:
        resultados = get_materias_tipos_juicios(
            database=database,
            materia_id=materia_id,
            materia_clave=materia_clave,
        )
    except MyAnyError as error:
        return custom_list_success_false(error)
    return paginate(resultados)
