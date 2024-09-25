"""
Tesis Jurisprudencias v3, esquemas de pydantic
"""

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class TesisJurisprudenciaOut(BaseModel):
    """Esquema para entregar tesis jurisprudencias"""

    id: int = Field(default=None)
    distrito_id: int = Field(default=None)
    distrito_clave: str = Field(default=None)
    distrito_nombre: str = Field(default=None)
    distrito_nombre_corto: str = Field(default=None)
    autoridad_id: int = Field(default=None)
    autoridad_clave: str = Field(default=None)
    autoridad_descripcion: str = Field(default=None)
    autoridad_descripcion_corta: str = Field(default=None)
    epoca_id: int = Field(default=None)
    epoca_nombre: str = Field(default=None)
    materia_id: int = Field(default=None)
    materia_clave: str = Field(default=None)
    materia_nombre: str = Field(default=None)
    titulo: str = Field(default=None)
    subtitulo: str = Field(default=None)
    tipo: str = Field(default=None)
    estado: str = Field(default=None)
    clave_control: str = Field(default=None)
    clase: str = Field(default=None)
    rubro: str = Field(default=None)
    texto: str = Field(default=None)
    precedentes: str = Field(default=None)
    votacion: str = Field(default=None)
    votos_particulares: str = Field(default=None)
    aprobacion_fecha: date = Field(default=None)
    publicacion_tiempo: datetime = Field(default=None)
    aplicacion_tiempo: datetime = Field(default=None)
    model_config = ConfigDict(from_attributes=True)


class OneTesisJurisprudenciaOut(TesisJurisprudenciaOut, OneBaseOut):
    """Esquema para entregar un tesis jurisprudencia"""
