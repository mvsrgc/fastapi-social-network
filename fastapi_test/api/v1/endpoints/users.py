from typing import Annotated

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from fastapi_test.api.deps import get_current_active_user
from fastapi_test.core.security import get_password_hash
from fastapi_test.db import engine
from fastapi_test.models import User, UserCreate, UserRead

router = APIRouter()


@router.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    with Session(engine) as session:
        db_user = User.from_orm(user)
        db_user.password = get_password_hash(user.password)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user


@router.get("/users/", response_model=list[UserRead])
def get_users(current_user: Annotated[User, Depends(get_current_active_user)]):
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users


@router.get("/users/me", response_model=UserRead)
def get_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user
