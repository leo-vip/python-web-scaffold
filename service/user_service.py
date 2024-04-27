from sqlalchemy.orm import Session

import core.models.models as models
from core import util
from core.schemas.user_schema import UserIn


def get_user(db: Session, user_id: int):
    return db.query(models.TUser).filter(models.TUser.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> models.TUser:
    return db.query(models.TUser).filter(models.TUser.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TUser).offset(skip).limit(limit).all()


def create_user(db: Session, user_in: UserIn) -> models.TUser:
    hashed_password = util.md5_hash(user_in.password)
    db_user = models.TUser(**user_in.dict(), id=util.get_unique_id())
    db_user.password = hashed_password
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user