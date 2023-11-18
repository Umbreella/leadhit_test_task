import pytest
from motor.core import AgnosticCollection
from motor.motor_asyncio import AsyncIOMotorDatabase

from src.enums.collections import Collections
from src.enums.type_field import TypeField


@pytest.fixture
async def forms(database: AsyncIOMotorDatabase) -> None:
    forms: AgnosticCollection = database.get_collection(name=Collections.forms)

    await forms.insert_one(
        {
            'name': 'user_template',
            'user_name': TypeField.text,
            'user_birth_date': TypeField.date,
            'user_email': TypeField.email,
            'user_phone': TypeField.phone,
        },
    )
    await forms.insert_one(
        {
            'name': 'order_template',
            'order_description': TypeField.text,
            'order_date': TypeField.date,
            'order_email': TypeField.email,
        },
    )
