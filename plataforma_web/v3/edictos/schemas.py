"""
Edictos v3, esquemas de pydantic
"""

from datetime import date

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class EdictoOut(BaseModel):
    """Esquema para entregar edictos"""

    id: int = Field(default=None)
    distrito_id: int = Field(default=None)
    distrito_clave: str = Field(default=None)
    distrito_nombre: str = Field(default=None)
    distrito_nombre_corto: str = Field(default=None)
    autoridad_id: int = Field(default=None)
    autoridad_clave: str = Field(default=None)
    autoridad_descripcion: str = Field(default=None)
    autoridad_descripcion_corta: str = Field(default=None)
    fecha: date = Field(default=None)
    descripcion: str = Field(default=None)
    expediente: str = Field(default=None)
    numero_publicacion: str = Field(default=None)
    archivo: str = Field(default=None)
    url: str = Field(default=None)
    model_config = ConfigDict(from_attributes=True)


class OneEdictoOut(EdictoOut, OneBaseOut):
    """Esquema para entregar un edicto"""
