"""
Abogados v3, esquemas de pydantic
"""

from datetime import date

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class AbogadoOut(BaseModel):
    """Esquema para entregar abogados"""

    id: int = Field(default=None)
    fecha: date = Field(default=None)
    numero: str = Field(default=None)
    libro: str = Field(default=None)
    nombre: str = Field(default=None)
    model_config = ConfigDict(from_attributes=True)


class OneAbogadoOut(AbogadoOut, OneBaseOut):
    """Esquema para entregar un abogado"""
