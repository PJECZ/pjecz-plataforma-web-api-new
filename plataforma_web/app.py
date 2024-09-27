"""
PJECZ Plataforma Web API new
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from fastapi_pagination import add_pagination
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from lib.limiter import limiter, settings
from plataforma_web.v3.abogados.paths import abogados
from plataforma_web.v3.audiencias.paths import audiencias
from plataforma_web.v3.autoridades.paths import autoridades
from plataforma_web.v3.distritos.paths import distritos
from plataforma_web.v3.edictos.paths import edictos
from plataforma_web.v3.epocas.paths import epocas
from plataforma_web.v3.glosas.paths import glosas
from plataforma_web.v3.listas_de_acuerdos.paths import listas_de_acuerdos
from plataforma_web.v3.materias.paths import materias
from plataforma_web.v3.materias_tipos_juicios.paths import materias_tipos_juicios
from plataforma_web.v3.peritos.paths import peritos
from plataforma_web.v3.peritos_tipos.paths import peritos_tipos
from plataforma_web.v3.redam.paths import redam
from plataforma_web.v3.repsvm_agresores.paths import repsvm_agresores
from plataforma_web.v3.sentencias.paths import sentencias
from plataforma_web.v3.tesis_jurisprudencias.paths import tesis_jurisprudencias
from plataforma_web.v3.ubicaciones_expedientes.paths import ubicaciones_expedientes


def create_app() -> FastAPI:
    """Crea la aplicación FastAPI"""

    # FastAPI
    app = FastAPI(
        title="PJECZ Plataforma Web API new",
        description="API que proporciona datos para las consultas del sitio web.",
        docs_url="/docs",
        redoc_url=None,
    )

    # CORSMiddleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.origins.split(","),
        allow_credentials=False,
        allow_methods=["GET"],
        allow_headers=["*"],
    )

    # Rutas
    app.include_router(abogados)
    app.include_router(audiencias)
    app.include_router(autoridades)
    app.include_router(distritos)
    app.include_router(edictos)
    app.include_router(epocas)
    app.include_router(glosas)
    app.include_router(listas_de_acuerdos)
    app.include_router(materias)
    app.include_router(materias_tipos_juicios)
    app.include_router(peritos)
    app.include_router(peritos_tipos)
    app.include_router(redam)
    app.include_router(repsvm_agresores)
    app.include_router(sentencias)
    app.include_router(tesis_jurisprudencias)
    app.include_router(ubicaciones_expedientes)

    # Paginar
    add_pagination(app)

    # Limitar peticiones
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

    # Mensaje de Bienvenida
    @app.get("/")
    async def root():
        """Mensaje de Bienvenida"""
        return {"message": "API que proporciona datos para las consultas del sitio web."}

    @app.get("/robots.txt", response_class=PlainTextResponse)
    async def robots():
        """robots.txt to disallow all agents"""
        return """User-agent: *\nDisallow: /"""

    # Entregar
    return app
