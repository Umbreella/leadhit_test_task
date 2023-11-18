import asyncio

from motor.core import AgnosticCollection

from src.database import db
from src.enums.collections import Collections
from src.enums.type_field import TypeField


async def main():
    forms: AgnosticCollection = db.get_collection(name=Collections.forms)

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


if __name__ == '__main__':
    asyncio.run(main())
