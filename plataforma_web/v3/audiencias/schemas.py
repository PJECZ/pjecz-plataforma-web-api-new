"""
Audiencias v3, esquemas de pydantic
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class AudienciaOut(BaseModel):
    """Esquema para entregar audiencias"""

    id: int = Field(default=None)
    distrito_id: int = Field(default=None)
    distrito_clave: str = Field(default=None)
    distrito_nombre: str = Field(default=None)
    distrito_nombre_corto: str = Field(default=None)
    autoridad_id: int = Field(default=None)
    autoridad_clave: str = Field(default=None)
    autoridad_descripcion: str = Field(default=None)
    autoridad_descripcion_corta: str = Field(default=None)
    tiempo: datetime = Field(default=None)
    tipo_audiencia: str = Field(default=None)
    expediente: str = Field(default=None)
    actores: str = Field(default=None)
    demandados: str = Field(default=None)
    sala: str = Field(default=None)
    caracter: str = Field(default=None)
    causa_penal: str = Field(default=None)
    delitos: str = Field(default=None)
    toca: str = Field(default=None)
    expediente_origen: str = Field(default=None)
    imputados: str = Field(default=None)
    origen: str = Field(default=None)
    model_config = ConfigDict(from_attributes=True)


class OneAudienciaOut(AudienciaOut, OneBaseOut):
    """Esquema para entregar una audiencia"""
