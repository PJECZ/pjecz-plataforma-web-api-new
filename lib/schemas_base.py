"""
Schemas Base
"""

from pydantic import BaseModel, Field


class OneBaseOut(BaseModel):
    """BaseOut"""

    success: bool = Field(default=True)
    message: str = Field(default="Success")
