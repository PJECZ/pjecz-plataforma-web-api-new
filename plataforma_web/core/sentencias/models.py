"""
Sentencias, modelos
"""

from datetime import date
from typing import Optional

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Sentencia(Base, UniversalMixin):
    """Sentencia"""

    # Nombre de la tabla
    __tablename__ = "sentencias"

    # Clave primaria
    id: Mapped[int] = mapped_column(primary_key=True)

    # Claves foráneas
    autoridad_id: Mapped[int] = mapped_column(ForeignKey("autoridades.id"))
    autoridad: Mapped["Autoridad"] = relationship(back_populates="sentencias")
    materia_tipo_juicio_id: Mapped[int] = mapped_column(ForeignKey("materias_tipos_juicios.id"))
    materia_tipo_juicio: Mapped["MateriaTipoJuicio"] = relationship(back_populates="sentencias")

    # Columnas
    sentencia: Mapped[str] = mapped_column(String(16))
    sentencia_fecha: Mapped[Optional[date]] = mapped_column(Date(), index=True)
    expediente: Mapped[str] = mapped_column(String(16))
    expediente_anio: Mapped[int]
    expediente_num: Mapped[int]
    fecha: Mapped[date] = mapped_column(Date(), index=True)
    descripcion: Mapped[str] = mapped_column(String(1024))
    es_perspectiva_genero: Mapped[bool] = mapped_column(default=False)
    archivo: Mapped[str] = mapped_column(String(256), default="", server_default="")
    url: Mapped[str] = mapped_column(String(512), default="", server_default="")

    @property
    def distrito_id(self):
        """Distrito ID"""
        return self.autoridad.distrito_id

    @property
    def distrito_clave(self):
        """Distrito clave"""
        return self.autoridad.distrito.clave

    @property
    def distrito_nombre(self):
        """Distrito nombre"""
        return self.autoridad.distrito.nombre

    @property
    def distrito_nombre_corto(self):
        """Distrito nombre corto"""
        return self.autoridad.distrito.nombre_corto

    @property
    def autoridad_clave(self):
        """Autoridad clave"""
        return self.autoridad.clave

    @property
    def autoridad_descripcion(self):
        """Autoridad descripción"""
        return self.autoridad.descripcion

    @property
    def autoridad_descripcion_corta(self):
        """Autoridad descripción corta"""
        return self.autoridad.descripcion_corta

    @property
    def materia_id(self):
        """Materia ID"""
        return self.materia_tipo_juicio.materia_id

    @property
    def materia_nombre(self):
        """Nombre de la materia"""
        return self.materia_tipo_juicio.materia.nombre

    @property
    def materia_tipo_juicio_descripcion(self):
        """Materia-Tipo de Juicio descripción"""
        return self.materia_tipo_juicio.descripcion

    def __repr__(self):
        """Representación"""
        return f"<Sentencia {self.id}>"
