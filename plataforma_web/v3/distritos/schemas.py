"""
Distritos v3, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class DistritoOut(BaseModel):
    """Esquema para entregar distritos"""

    id: int = Field(default=None)
    clave: str = Field(default=None)
    nombre: str = Field(default=None)
    nombre_corto: str = Field(default=None)
    es_distrito_judicial: bool = Field(default=None)
    es_distrito: bool = Field(default=None)
    es_jurisdiccional: bool = Field(default=None)
    model_config = ConfigDict(from_attributes=True)


class OneDistritoOut(DistritoOut, OneBaseOut):
    """Esquema para entregar un distrito"""
