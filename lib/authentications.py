"""
Autentificaciones
"""
import re

from cryptography.fernet import Fernet
from fastapi import HTTPException, Depends
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel

EMAIL_REGEXP = r"^[\w.-]+@[\w.-]+\.\w+$"
KEY = b"vB2n4b8q6zu5xmBw2AM-1DG78xcS1dU7NPL9Q7BXzZU="
X_API_KEY = APIKeyHeader(name="X-Api-Key")

fernet_cipher = Fernet(KEY)


def encrypt_email(email: str) -> str:
    """Encriptar email"""

    return fernet_cipher.encrypt(email.encode()).decode()


def decrypt_email(email: str) -> str:
    """Desencriptar email"""

    return fernet_cipher.decrypt(email.encode()).decode()


class Usuario(BaseModel):
    """Usuario"""

    api_key: str
    email: str


async def get_current_user(api_key: str = Depends(X_API_KEY)) -> Usuario:
    """Obtener usuario actual"""

    # Desencriptar api_key para obtener email
    try:
        email = decrypt_email(api_key)
    except Exception as error:
        raise HTTPException(status_code=403, detail="API Key inválida")

    # Validar email
    if not re.match(EMAIL_REGEXP, email):
        raise HTTPException(status_code=403, detail="API Key inválida porque el email no es válido")

    # Que el email sea anonymous@server.net
    if email != "anonymous@server.net":
        raise HTTPException(status_code=403, detail="API Key no autorizada")

    # Entregar
    return Usuario(api_key=api_key, email="anonymous@server.net")
