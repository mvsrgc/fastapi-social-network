import uuid as uuid_pkg

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    username: str = Field(index=True)
    email: EmailStr = Field(index=True)
    is_active: bool = Field(default=True)


class User(UserBase, table=True):
    id: uuid_pkg.UUID | None = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True
    )
    password: str


class UserCreate(UserBase):
    password: str = Field()


class UserRead(UserBase):
    id: uuid_pkg.UUID
