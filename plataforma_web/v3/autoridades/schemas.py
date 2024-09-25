"""
Autoridades v3, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class AutoridadOut(BaseModel):
    """Esquema para entregar autoridades"""

    id: int = Field(default=None)
    distrito_id: int = Field(default=None)
    distrito_clave: str = Field(default=None)
    distrito_nombre: str = Field(default=None)
    distrito_nombre_corto: str = Field(default=None)
    materia_id: int = Field(default=None)
    materia_clave: str = Field(default=None)
    materia_nombre: str = Field(default=None)
    clave: str = Field(default=None)
    descripcion: str = Field(default=None)
    descripcion_corta: str = Field(default=None)
    es_cemasc: bool = Field(default=None)
    es_creador_glosas: bool = Field(default=None)
    es_defensoria: bool = Field(default=None)
    es_jurisdiccional: bool = Field(default=None)
    es_notaria: bool = Field(default=None)
    organo_jurisdiccional: str = Field(default=None)
    audiencia_categoria: str = Field(default=None)
    model_config = ConfigDict(from_attributes=True)


class OneAutoridadOut(AutoridadOut, OneBaseOut):
    """Esquema para entregar una autoridad"""
