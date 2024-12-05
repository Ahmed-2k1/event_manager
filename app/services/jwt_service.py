# app/services/jwt_service.py
from builtins import dict, str
import jwt
from datetime import datetime, timedelta
from settings.config import settings


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    """
    Create a JWT access token with an optional expiration.

    Args:
        data (dict): The payload data to include in the token.
        expires_delta (timedelta, optional): The duration for which the token is valid.

    Returns:
        str: The encoded JWT access token.
    """
    to_encode = data.copy()

    # Ensure 'role' is uppercase before encoding
    if 'role' in to_encode:
        to_encode['role'] = to_encode['role'].upper()

    # Set expiration time
    expiration = datetime.utcnow(
    ) + (expires_delta or timedelta(minutes=settings.access_token_expire_minutes))
    to_encode.update({"exp": expiration})

    # Encode the JWT
    return jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)


def decode_token(token: str):
    """
    Decode a JWT token.

    Args:
        token (str): The JWT token to decode.

    Returns:
        dict | None: Decoded token data if valid; otherwise, None.
    """
    try:
        return jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
    except jwt.PyJWTError:
        return None