"""
PJECZ Plataforma Web API
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from .v3.autoridades.paths import autoridades
from .v3.distritos.paths import distritos

ORIGINS = [
    "http://localhost:5000",
    "http://localhost:8001",
    "http://127.0.0.1:5000",
    "http://127.0.0.1:8001",
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

# Paginación
add_pagination(app)


@app.get("/")
async def root():
    """Mensaje de Bienvenida"""
    return {"message": "Bienvenido a PJECZ Plataforma Web API."}