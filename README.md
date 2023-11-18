# LeadHit (REST-API)

## Backend

![python](https://img.shields.io/badge/python-3776AB?logo=python&logoColor=white&style=for-the-badge&)
![fastapi](https://img.shields.io/badge/fastapi-009688?logo=fastapi&logoColor=white&style=for-the-badge&)
![sqlalchemy](https://img.shields.io/badge/sqlalchemy_+_alembic-d71f00?logo=sqlite&logoColor=white&style=for-the-badge&)
![poetry](https://img.shields.io/badge/poetry-60A5FA?logo=poetry&logoColor=white&style=for-the-badge&)

## Testing

![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![codecov](https://img.shields.io/codecov/c/github/Umbreella/leadhit_test_task?style=for-the-badge&logo=codecov)

## Database

![mongo](https://img.shields.io/badge/mongodb-47A248?logo=mongodb&logoColor=white&style=for-the-badge&)

## Cloud & CI/CD

![docker](https://img.shields.io/badge/docker-2496ED?logo=docker&logoColor=white&style=for-the-badge&)
![githubactions](https://img.shields.io/badge/githubactions-2088FF?logo=githubactions&logoColor=white&style=for-the-badge&)

---

## Description

[Task Description](TaskDescription.pdf)

## Getting Started

### Environment variables

To run the application, you need to set all the environment variables:

* **[.env.fastapi](./src/config.py)**
* **[.env.mongodb](https://www.mongodb.com/compatibility/docker)**
    * MONGO_INITDB_ROOT_USERNAME
    * MONGO_INITDB_ROOT_PASSWORD

## Docker

1. docker-compose.yml

```yaml
version: "3"

services:
  mongodb:
    image: mongodb/mongodb-community-server:7.0.1-ubi8
    container_name: mongodb
    ports:
      - 27017:27017
    environment:
      - MONGO_INITDB_ROOT_USERNAME=mongodb
      - MONGO_INITDB_ROOT_PASSWORD=mongodb

  leadhit_test_task:
    image: umbreella/leadhit_test_task:latest
    container_name: leadhit_test_task
    ports:
      - 8080:8080
    environment:
      - TYPE_ENV=docker
    depends_on:
      - mongodb
```

2. Docker-compose run

```commandline
docker-compose up -d
```

3. Open bash in container

```commandline
docker exec -it leadhit_test_task bash
```

4. Run script for insert date

```commandline
python3 scripts/fixture_forms.py
```

## Endpoints

* REST-API Docs - [urls.py](src/api/urls.py)