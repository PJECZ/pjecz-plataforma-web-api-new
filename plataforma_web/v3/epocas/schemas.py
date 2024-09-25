"""
Epocas v3, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class EpocaOut(BaseModel):
    """Esquema para entregar epocas"""

    id: int = Field(default=None)
    nombre: str = Field(default=None)
    model_config = ConfigDict(from_attributes=True)


class OneEpocaOut(EpocaOut, OneBaseOut):
    """Esquema para entregar un epoca"""
