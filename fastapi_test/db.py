import os

from sqlmodel import SQLModel, create_engine

DATABASE_URL = os.environ["DATABASE_URL"]


engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    # SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
