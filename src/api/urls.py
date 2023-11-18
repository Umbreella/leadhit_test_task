from fastapi import FastAPI

from src.api.form import Form


def add_routers(app: FastAPI) -> None:
    app.add_route(
        path='/api/form/validate',
        route=Form.validate_form,
        methods=['POST'],
    )
