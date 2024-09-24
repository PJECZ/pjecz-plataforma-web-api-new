"""
Peritos v3, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class PeritoOut(BaseModel):
    """Esquema para entregar peritos"""

    id: int = Field(default=None)
    distrito_id: int = Field(default=None)
    distrito_clave: str = Field(default=None)
    distrito_nombre: str = Field(default=None)
    distrito_nombre_corto: str = Field(default=None)
    perito_tipo_id: int = Field(default=None)
    perito_tipo_nombre: str = Field(default=None)
    nombre: str = Field(default=None)
    domicilio: str = Field(default=None)
    telefono_fijo: str = Field(default=None)
    telefono_celular: str = Field(default=None)
    email: str = Field(default=None)
    notas: str = Field(default=None)
    model_config = ConfigDict(from_attributes=True)


class OnePeritoOut(PeritoOut, OneBaseOut):
    """Esquema para entregar un perito"""
