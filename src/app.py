from fastapi import FastAPI

from src.api.urls import add_routers


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(
        docs_url='/api/docs',
    )

    add_routers(app=app)

    return app
