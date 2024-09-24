"""
Sentencias v3, esquemas de pydantic
"""

from datetime import date

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class SentenciaOut(BaseModel):
    """Esquema para entregar sentencias"""

    id: int = Field(default=None)
    distrito_id: int = Field(default=None)
    distrito_clave: str = Field(default=None)
    distrito_nombre: str = Field(default=None)
    distrito_nombre_corto: str = Field(default=None)
    autoridad_id: int = Field(default=None)
    autoridad_clave: str = Field(default=None)
    autoridad_descripcion: str = Field(default=None)
    autoridad_descripcion_corta: str = Field(default=None)
    materia_tipo_juicio_id: int = Field(default=None)
    materia_tipo_juicio_descripcion: str = Field(default=None)
    sentencia: str = Field(default=None)
    sentencia_fecha: date = Field(default=None)
    expediente: str = Field(default=None)
    fecha: date = Field(default=None)
    descripcion: str = Field(default=None)
    es_perspectiva_genero: bool = Field(default=None)
    archivo: str = Field(default=None)
    url: str = Field(default=None)
    model_config = ConfigDict(from_attributes=True)


class OneSentenciaOut(SentenciaOut, OneBaseOut):
    """Esquema para entregar una sentencia"""
