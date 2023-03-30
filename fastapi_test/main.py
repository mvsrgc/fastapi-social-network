from fastapi import FastAPI

from fastapi_test.api.v1.api import api_router
from fastapi_test.core.config import settings
from fastapi_test.db import init_db

app = FastAPI(openapi_url=f"{settings.API_V1_PREFIX}/openapi.json")


@app.on_event("startup")
def on_startup():
    init_db()


app.include_router(api_router, prefix=settings.API_V1_PREFIX)
