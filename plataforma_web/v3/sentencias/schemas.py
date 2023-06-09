"""
Sentencias v3, esquemas de pydantic
"""
from datetime import date

from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class SentenciaOut(BaseModel):
    """Esquema para entregar sentencias"""

    id: int | None
    distrito_id: int | None
    distrito_clave: str | None
    distrito_nombre: str | None
    distrito_nombre_corto: str | None
    autoridad_id: int | None
    autoridad_clave: str | None
    autoridad_descripcion: str | None
    autoridad_descripcion_corta: str | None
    materia_tipo_juicio_id: int | None
    materia_tipo_juicio_descripcion: str | None
    sentencia: str | None
    sentencia_fecha: date | None
    expediente: str | None
    fecha: date | None
    descripcion: str | None
    es_perspectiva_genero: bool | None
    archivo: str | None
    url: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneSentenciaOut(SentenciaOut, OneBaseOut):
    """Esquema para entregar una sentencia"""
