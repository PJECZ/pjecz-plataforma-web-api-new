# pjecz-plataforma-web-api-new

API que proporciona datos para el sitio web pjecz.gob.mx

## Mejores practicas

Usa las recomendaciones de [I've been abusing HTTP Status Codes in my APIs for years](https://blog.slimjim.xyz/posts/stop-using-http-codes/)

### Respuesta exitosa

Status code: **200**

Body que entrega un listado

    {
        "success": true,
        "message": "Success",
        "result": {
            "total": 2812,
            "items": [ { "id": 1, ... } ],
            "limit": 100,
            "offset": 0
        }
    }

Body que entrega un item

    {
        "success": true,
        "message": "Success",
        "id": 123,
        ...
    }

### Respuesta fallida: registro no encontrado

Status code: **200**

Body

    {
        "success": false,
        "message": "No employee found for ID 100"
    }

### Respuesta fallida: ruta incorrecta

Status code: **404**

## Configure Poetry

Por defecto, con **poetry** el entorno se guarda en un directorio en `~/.cache/pypoetry/virtualenvs`

Modifique para que el entorno se guarde en el mismo directorio que el proyecto

    poetry config --list
    poetry config virtualenvs.in-project true

Verifique que este en True

    poetry config virtualenvs.in-project

## Configuracion

**Para produccion** se toman los secretos desde **Google Cloud** con _secret manager_

**Para desarrollo** hay que crear un archivo para las variables de entorno `.env`

    # Base de datos
    DB_HOST=
    DB_PORT=
    DB_NAME=
    DB_USER=
    DB_PASS=

    # Huso horario
    TZ=America/Mexico_City

Cree un archivo `.bashrc` que se puede usar en el perfil de **Konsole**

    if [ -f ~/.bashrc ]
    then
        . ~/.bashrc
    fi

    if command -v figlet &> /dev/null
    then
        figlet PJECZ Plataforma Web API
    else
        echo "== PJECZ Plataforma Web API"
    fi
    echo

    if [ -f .env ]
    then
        echo "-- Variables de entorno"
        export $(grep -v '^#' .env | xargs)
        echo "   DB_HOST: ${DB_HOST}"
        echo "   DB_PORT: ${DB_PORT}"
        echo "   DB_NAME: ${DB_NAME}"
        echo "   DB_USER: ${DB_USER}"
        echo "   DB_PASS: ${DB_PASS}"
        echo "   TZ: ${TZ}"
        echo
        export PGHOST=$DB_HOST
        export PGPORT=$DB_PORT
        export PGDATABASE=$DB_NAME
        export PGUSER=$DB_USER
        export PGPASSWORD=$DB_PASS
    fi

    if [ -d .venv ]
    then
        echo "-- Python Virtual Environment"
        source .venv/bin/activate
        echo "   $(python3 --version)"
        export PYTHONPATH=$(pwd)
        echo "   PYTHONPATH: ${PYTHONPATH}"
        echo
        alias black="black --config pyproject.toml"
        alias arrancar="uvicorn --host=127.0.0.1 --port 8001 --reload plataforma_web.app:app"
        echo "-- Ejecutar FastAPI 127.0.0.1:8001"
        echo "   arrancar"
        echo
    fi

    if [ -f app.yaml ]
    then
        echo "-- Subir a Google Cloud"
        echo "   poetry export -f requirements.txt --output requirements.txt --without-hashes"
        echo "   gcloud app deploy"
        echo
    fi

## Instalacion

En Fedora Linux agregue este software

    sudo dnf -y groupinstall "Development Tools"
    sudo dnf -y install glibc-langpack-en glibc-langpack-es
    sudo dnf -y install pipenv poetry python3-virtualenv
    sudo dnf -y install python3-devel python3-docs python3-idle
    sudo dnf -y install python3.11

Clone el repositorio

    cd ~/Documents/GitHub/PJECZ
    git clone https://github.com/PJECZ/pjecz-plataforma-web-api-new.git
    cd pjecz-plataforma-web-api-new

Instale el entorno virtual con **Python 3.11** y los paquetes necesarios

    python3.11 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install wheel
    poetry install

## Arrancar local para desarrollo

Ejecute `arrancar` que contiene el comando y parametros para arrancar el servicio

    arrancar

## Google Cloud deployment

Relice estos pasos para subir a Google Cloud App Engine

Crear el archivo `requirements.txt`

    poetry export -f requirements.txt --output requirements.txt --without-hashes

Y subir a Google Cloud

    gcloud app deploy
