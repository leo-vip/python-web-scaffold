import hashlib
import uuid
from datetime import datetime, timedelta
from typing import Union

from jose import jwt

SECRET_KEY = "e2a14f27-75f7-473b-ad7e-673361ff3018a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"


def md5_hash(value: str):
    if value is None:
        return None

    return hashlib.md5(value.encode(encoding='UTF-8')).hexdigest()


def encode_jwt_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_jwt_access_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload


def get_unique_id():
    return str(uuid.uuid4()).replace("-", "")


files_cache = {}


def get_templates_file(name, force=False):
    html = files_cache.get(name)
    if html is None or force:
        html = open(f"templates/{name}",encoding='utf-8').read()
        files_cache[name] = html
    return html
