from fastapi import FastAPI

from app.api.routes.router import api


def get_app() -> FastAPI:
    fast_app = FastAPI()
    fast_app.include_router(api)

    return fast_app

app = get_app()
