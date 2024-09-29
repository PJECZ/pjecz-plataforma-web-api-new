"""
Epocas v3, rutas (paths)
"""

from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_username
from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList, custom_list_success_false
from plataforma_web.v3.epocas.crud import get_epoca, get_epocas
from plataforma_web.v3.epocas.schemas import ItemEpocaOut, OneEpocaOut

epocas = APIRouter(prefix="/v3/epocas", tags=["tesis jurisprudencias"])


@epocas.get("/{epoca_id}", response_model=OneEpocaOut)
async def detalle_epoca(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
    epoca_id: int,
):
    """Detalle de una epoca a partir de su id"""
    try:
        epoca = get_epoca(database, epoca_id)
    except MyAnyError as error:
        return OneEpocaOut(success=False, message=str(error))
    return OneEpocaOut.model_validate(epoca)


@epocas.get("", response_model=CustomList[ItemEpocaOut])
async def listado_epocas(
    database: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Usuario, Depends(get_current_username)],
):
    """Listado de epocas"""
    try:
        resultados = get_epocas(database)
    except MyAnyError as error:
        return custom_list_success_false(error)
    return paginate(resultados)
