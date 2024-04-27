from datetime import timedelta

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError
from requests import Session
from starlette import status

from core import util, db_core
from core.exceptions import get_error_message_response
from core.models import models
from core.util import encode_jwt_access_token
from routes.base import app
from service import user_service
from core.schemas.user_schema import TokenData, UserOut, UserIn

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def get_db():
    db = db_core.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(db=Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = util.decode_jwt_access_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = user_service.get_user_by_email(db, token_data.username)

    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: models.TUser = Depends(get_current_user)):
    if current_user.status != 0:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/auth/token", tags=['Manager'])
async def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_service.get_user_by_email(db, form_data.username)
    if user is None or util.md5_hash(form_data.password) != user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    if user.status != 0:
        raise HTTPException(status_code=402, detail="User status disabled.")

    access_token_expires = timedelta(days=30)
    access_token = encode_jwt_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "Bearer", "refresh_token": access_token}


@app.get("/auth/user_info", response_model=UserOut, tags=['Manager'])
def code_url(current_user: models.TUser = Depends(get_current_active_user)):
    return current_user

@app.post("/auth/create_user", response_model=UserOut, tags=['Manager'])
def user_create(user_in: UserIn, db: Session = Depends(get_db)):
    if user_service.get_user_by_email(db, user_in.email) is not None:
        return get_error_message_response(400, 400, "Email already registered")
    user: models.TUser = user_service.create_user(db, user_in)

    return user