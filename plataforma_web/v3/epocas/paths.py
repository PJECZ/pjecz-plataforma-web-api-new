"""
Epocas v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_user
from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList, custom_list_success_false

from .crud import get_epocas, get_epoca
from .schemas import EpocaOut, OneEpocaOut

epocas = APIRouter(prefix="/v3/epocas", tags=["tesis jurisprudencias"])


@epocas.get("", response_model=CustomList[EpocaOut])
async def listado_epocas(
    db: DatabaseSession,
    current_user: Annotated[Usuario, Depends(get_current_user)],
):
    """Listado de epocas"""
    try:
        resultados = get_epocas(db=db)
    except MyAnyError as error:
        return custom_list_success_false(error)
    return paginate(resultados)


@epocas.get("/{epoca_id}", response_model=OneEpocaOut)
async def detalle_epoca(
    db: DatabaseSession,
    current_user: Annotated[Usuario, Depends(get_current_user)],
    epoca_id: int,
):
    """Detalle de una epoca a partir de su id"""
    try:
        epoca = get_epoca(db, epoca_id)
    except MyAnyError as error:
        return OneEpocaOut(success=False, message=str(error))
    return OneEpocaOut.from_orm(epoca)
