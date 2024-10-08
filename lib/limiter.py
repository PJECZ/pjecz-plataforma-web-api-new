"""
Limiter
"""

from slowapi import Limiter
from slowapi.util import get_remote_address

from config.settings import get_settings

settings = get_settings()

limiter = Limiter(key_func=get_remote_address, storage_uri=settings.redis)
