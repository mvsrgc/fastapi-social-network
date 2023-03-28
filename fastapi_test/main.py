from db import init_db
from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from fastapi_test.db import get_session
from fastapi_test.models import User, UserCreate

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/users", response_model=list[User])
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return [User(name=user.name, password=user.password) for user in users]


@app.post("/users")
async def add_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    user = User(name=user.name, password=user.password)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user