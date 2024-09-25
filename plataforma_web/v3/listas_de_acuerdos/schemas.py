"""
Listas de Acuerdos v3, esquemas de pydantic
"""

from datetime import date

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ListaDeAcuerdoOut(BaseModel):
    """Esquema para entregar listas de acuerdos"""

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
    archivo: str = Field(default=None)
    url: str = Field(default=None)
    model_config = ConfigDict(from_attributes=True)


class OneListaDeAcuerdoOut(ListaDeAcuerdoOut, OneBaseOut):
    """Esquema para entregar una lista de acuerdo"""
