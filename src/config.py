import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGODB_HOST: str
    MONGODB_PORT: int = 27017
    MONGODB_DATABASE: str = 'template'
    MONGODB_USERNAME: str = 'mongodb'
    MONGODB_PASSWORD: str = 'mongodb'


class DockerSettings(Settings):
    MONGODB_HOST: str = 'mongodb'


class LocalSettings(Settings):
    MONGODB_HOST: str = '127.0.0.1'


def get_settings() -> DockerSettings | LocalSettings:
    settings: dict = {
        'docker': DockerSettings,
        'local': LocalSettings,
    }

    return settings[os.environ['TYPE_ENV']]()


settings = get_settings()
