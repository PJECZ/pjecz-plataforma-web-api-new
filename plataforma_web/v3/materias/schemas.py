"""
Materias v3, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class MateriaOut(BaseModel):
    """Esquema para entregar materias"""

    id: int = Field(default=None)
    clave: str = Field(default=None)
    nombre: str = Field(default=None)
    model_config = ConfigDict(from_attributes=True)


class OneMateriaOut(MateriaOut, OneBaseOut):
    """Esquema para entregar una materia"""
