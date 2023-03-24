"""
Abogados v3, esquemas de pydantic
"""
from datetime import date

from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class AbogadoOut(BaseModel):
    """Esquema para entregar abogados"""

    id: int | None
    fecha: date | None
    numero: str | None
    libro: str | None
    nombre: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneAbogadoOut(AbogadoOut, OneBaseOut):
    """Esquema para entregar un abogado"""
