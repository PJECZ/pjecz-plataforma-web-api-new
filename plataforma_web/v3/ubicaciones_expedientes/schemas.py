"""
Ubicaciones de Expedientes v3, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class UbicacionExpedienteOut(BaseModel):
    """Esquema para entregar ubicaciones de expedientes"""

    id: int = Field(default=None)
    distrito_id: int = Field(default=None)
    distrito_clave: str = Field(default=None)
    distrito_nombre: str = Field(default=None)
    distrito_nombre_corto: str = Field(default=None)
    autoridad_id: int = Field(default=None)
    autoridad_clave: str = Field(default=None)
    autoridad_descripcion: str = Field(default=None)
    autoridad_descripcion_corta: str = Field(default=None)
    expediente: str = Field(default=None)
    ubicacion: str = Field(default=None)
    model_config = ConfigDict(from_attributes=True)


class OneUbicacionExpedienteOut(UbicacionExpedienteOut, OneBaseOut):
    """Esquema para entregar una ubicacion de expediente"""
