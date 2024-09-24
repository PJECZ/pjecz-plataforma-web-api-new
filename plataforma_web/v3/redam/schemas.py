"""
REDAM (Registro Estatal de Deudores Alimentarios Morosos) v3, esquemas de pydantic
"""

from datetime import date

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class RedamOut(BaseModel):
    """Esquema para entregar deudores alimentarios morosos"""

    id: int = Field(default=None)
    distrito_id: int = Field(default=None)
    distrito_clave: str = Field(default=None)
    distrito_nombre: str = Field(default=None)
    distrito_nombre_corto: str = Field(default=None)
    autoridad_id: int = Field(default=None)
    autoridad_clave: str = Field(default=None)
    autoridad_descripcion: str = Field(default=None)
    autoridad_descripcion_corta: str = Field(default=None)
    nombre: str = Field(default=None)
    expediente: str = Field(default=None)
    fecha: date = Field(default=None)
    observaciones: str = Field(default=None)
    model_config = ConfigDict(from_attributes=True)


class OneRedamOut(RedamOut, OneBaseOut):
    """Esquema para entregar un deudor alimentario moroso"""
