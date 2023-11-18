import re
from datetime import datetime
from typing import Any

from email_validator import validate_email
from fastapi import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.database import db
from src.enums.collections import Collections
from src.enums.type_field import TypeField
from src.utils.without_errors import without_errors


class Form:
    @classmethod
    async def validate_form(cls, request: Request) -> JSONResponse:
        payload: dict[str, Any]

        try:
            payload = await request.json()
        except Exception:
            return JSONResponse(
                content={
                    'detail': 'Request body is not JSON',
                },
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        mongo_query: dict[str, Any] = {
            key: cls._validate_field(value) for key, value in payload.items()
        }

        templates_collection = db.get_collection(name=Collections.forms)

        data = await templates_collection.find_one(mongo_query)

        if data:
            return JSONResponse(
                content={
                    'name': data.get('name'),
                },
            )

        return JSONResponse(
            content=mongo_query,
        )

    @classmethod
    def _validate_field(cls, value: Any) -> TypeField:
        if without_errors(datetime.strptime, value, '%d.%m.%Y'):
            return TypeField.date

        if without_errors(datetime.strptime, value, '%Y-%m-%d'):
            return TypeField.date

        pattern = re.compile(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', re.IGNORECASE)

        if pattern.match(value):
            return TypeField.phone

        if without_errors(validate_email, value):
            return TypeField.email

        return TypeField.text
