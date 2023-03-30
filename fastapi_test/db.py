from sqlmodel import SQLModel, create_engine

from fastapi_test.core.config import settings

db_url = settings.DATABASE_URL

engine = create_engine(db_url, echo=True)


def init_db():
    # SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
