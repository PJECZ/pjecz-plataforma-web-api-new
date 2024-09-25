"""
REPSVM Agresores v3, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class RepsvmAgresorOut(BaseModel):
    """Esquema para entregar agresores"""

    id: int = Field(default=None)
    distrito_id: int = Field(default=None)
    distrito_clave: str = Field(default=None)
    distrito_nombre: str = Field(default=None)
    distrito_nombre_corto: str = Field(default=None)
    consecutivo: int = Field(default=None)
    delito_generico: str = Field(default=None)
    delito_especifico: str = Field(default=None)
    nombre: str = Field(default=None)
    numero_causa: str = Field(default=None)
    pena_impuesta: str = Field(default=None)
    observaciones: str = Field(default=None)
    sentencia_url: str = Field(default=None)
    tipo_juzgado: str = Field(default=None)
    tipo_sentencia: str = Field(default=None)
    model_config = ConfigDict(from_attributes=True)


class OneRepsvmAgresorOut(RepsvmAgresorOut, OneBaseOut):
    """Esquema para entregar un agresor"""
