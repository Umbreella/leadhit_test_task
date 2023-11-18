import asyncio
from contextlib import ExitStack
from pkgutil import walk_packages

import pytest
from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from src.app import create_app
from src.config import settings
from tests import fixtures

module = fixtures
pytest_plugins = [
    *[
        package.name
        for package in walk_packages(
            path=module.__path__,
            prefix=module.__name__ + '.',
        )
    ],
]


@pytest.fixture(autouse=True)
def app():
    with ExitStack():
        yield create_app()


@pytest.fixture
async def client(app):
    async with AsyncClient(app=app, base_url='http://testserver') as c:
        yield c


@pytest.fixture(scope='session')
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def database() -> AsyncIOMotorDatabase:
    client: AsyncIOMotorClient = AsyncIOMotorClient(
        'mongodb://{username}:{password}@{host}:{port}'.format(
            username=settings.MONGODB_USERNAME,
            password=settings.MONGODB_PASSWORD,
            host=settings.MONGODB_HOST,
            port=settings.MONGODB_PORT,
        ),
    )

    database_name: str = '{db}_test'.format(
        db=settings.MONGODB_DATABASE,
    )

    try:
        client.drop_database(name_or_database=database_name)
    except Exception:
        pass

    return AsyncIOMotorDatabase(client=client, name=database_name)
