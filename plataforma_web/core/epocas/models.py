"""
Epocas, modelos
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Epoca(Base, UniversalMixin):
    """Epoca"""

    # Nombre de la tabla
    __tablename__ = "epocas"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Columnas
    nombre = Column(String(256), unique=True, nullable=False)

    # Hijos
    tesis_jurisprudencias = relationship("TesisJurisprudencia", back_populates="epoca")

    def __repr__(self):
        """Representación"""
        return f"<Epoca {self.id}>"
