# pjecz-plataforma-web-api-new

Nueva API que proporciona datos para el sitio web pjecz.gob.mx

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
    DB_HOST=NNN.NNN.NNN.NNN
    DB_PORT=5432
    DB_NAME=pjecz_plataforma_web
    DB_USER=readerpjeczplataformaweb
    DB_PASS=XXXXXXXXXXXXXXXX

    # Fernet key para cifrar y descifrar la API_KEY
    FERNET_KEY="XXXXXXXXXXXXXXXX"

    # CORS origins
    ORIGINS=http://localhost:3000,http://localhost:5000,http://127.0.0.1:3000,http://127.0.0.1:5000

    # Huso horario
    TZ=America/Mexico_City

    # Username es una dirección de correo electrónico para identificar al cliente
    USERNAME=anonymous@server.net

Cree un archivo `.bashrc` que se puede usar en el perfil de **Konsole**

    if [ -f ~/.bashrc ]
    then
        . ~/.bashrc
    fi

    if command -v figlet &> /dev/null
    then
        figlet Plataforma Web API New
    else
        echo "== Plataforma Web API New"
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
        echo "   ORIGINS: ${ORIGINS}"
        echo "   FERNET_KEY: ${FERNET_KEY}"
        echo "   TZ: ${TZ}"
        echo "   USERNAME: ${USERNAME}"
        echo
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
        alias arrancar="uvicorn --factory --host=127.0.0.1 --port 8001 --reload plataforma_web.app:create_app"
        echo "-- Ejecutar FastAPI 127.0.0.1:8001"
        echo "   arrancar"
        echo
    fi

    if [ -d tests ]
    then
        echo "-- Pruebas unitarias"
        echo "   python -m unittest discover tests"
        echo
    fi

    if [ -f .github/workflows/gcloud-app-deploy.yml ]
    then
        echo "-- Google Cloud"
        echo "   GitHub Actions hace el deploy en Google Cloud"
        echo "   Si hace cambios en pyproject.toml reconstruya requirements.txt"
        echo "   poetry export -f requirements.txt --output requirements.txt --without-hashes"
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

## Arrancar para desarrollo

Ejecute `arrancar` que es un alias dentro de `.bashrc`

    arrancar

## Pruebas

Para ejecutar las pruebas arranque el servidor y ejecute

    python -m unittest discover tests

## Contenedores

Esta incluido el archivo `Dockerfile` para construir la imagen

Va a usar el puerto **8001** para la API

Construir la imagen con el comando **podman**

```bash
podman build -t pjecz_plataforma_web_api .
```

Escribir el archivo `.env` con las variables de entorno

```ini
DB_HOST=NNN.NNN.NNN.NNN
DB_PORT=5432
DB_NAME=pjecz_plataforma_web
DB_USER=readerpjeczplataformaweb
DB_PASS=XXXXXXXXXXXXXXXX
FERNET_KEY="XXXXXXXXXXXXXXXX"
ORIGINS=*
USERNAME=anonymous@server.net
```

Arrancar el contenedor donde el puerto 8001 del contendor se dirige al puerto 7001 local

```bash
podman run --rm \
    --name pjecz_plataforma_web_api \
    -p 7001:8001 \
    --env-file .env \
    pjecz_plataforma_web_api
```

Arrancar el contenedor y dejar corriendo en el fondo

```bash
podman run -d \
    --name pjecz_plataforma_web_api \
    -p 7001:8001 \
    --env-file .env \
    pjecz_plataforma_web_api
```

Detener contenedor

```bash
podman container stop pjecz_plataforma_web_api
```

Eliminar contenedor

```bash
podman container rm pjecz_plataforma_web_api
```

## Google Cloud deployment

Este proyecto usa **GitHub Actions** para subir a **Google Cloud**

Para ello debe crear el archivo `requirements.txt`

    poetry export -f requirements.txt --output requirements.txt --without-hashes

Y subir a Google Cloud con

    gcloud app deploy
