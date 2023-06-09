"""
Materias v3, esquemas de pydantic
"""
from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class MateriaOut(BaseModel):
    """Esquema para entregar materias"""

    id: int | None
    clave: str | None
    nombre: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneMateriaOut(MateriaOut, OneBaseOut):
    """Esquema para entregar una materia"""
