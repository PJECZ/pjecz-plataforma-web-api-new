"""
Materias-Tipos de Juicios v3, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class MateriaTipoJuicioOut(BaseModel):
    """Esquema para entregar materias-tipos de juicios"""

    id: int = Field(default=None)
    materia_id: int = Field(default=None)
    materia_clave: str = Field(default=None)
    materia_nombre: str = Field(default=None)
    descripcion: str = Field(default=None)
    model_config = ConfigDict(from_attributes=True)


class OneMateriaTipoJuicioOut(MateriaTipoJuicioOut, OneBaseOut):
    """Esquema para entregar un materia-tipo de juicio"""
