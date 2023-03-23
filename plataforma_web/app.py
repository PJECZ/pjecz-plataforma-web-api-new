"""
PJECZ Plataforma Web API
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from .v3.autoridades.paths import autoridades
from .v3.distritos.paths import distritos
from .v3.edictos.paths import edictos
from .v3.listas_de_acuerdos.paths import listas_de_acuerdos
from .v3.materias.paths import materias
from .v3.materias_tipos_juicios.paths import materias_tipos_juicios
from .v3.sentencias.paths import sentencias

ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5000",
    "https://justiciadigital.gob.mx",
    "https://pjecz.gob.mx",
]

# FastAPI
app = FastAPI(
    title="PJECZ Plataforma Web API",
    description="API que proporciona datos para el sitio web pjecz.gob.mx.",
)

# CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(autoridades)
app.include_router(distritos)
app.include_router(edictos)
app.include_router(listas_de_acuerdos)
app.include_router(materias)
app.include_router(materias_tipos_juicios)
app.include_router(sentencias)

# Paginación
add_pagination(app)


@app.get("/")
async def root():
    """Mensaje de Bienvenida"""
    return {"message": "Bienvenido a PJECZ Plataforma Web API."}
