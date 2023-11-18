FROM python:3.11-slim-buster as builder

RUN pip install poetry

WORKDIR /usr/leadhit_test_task

COPY ./poetry.lock ./pyproject.toml ./

RUN poetry config virtualenvs.in-project true --local && poetry install --only main


FROM python:3.11-slim-buster as compile-image

WORKDIR /usr/leadhit_test_task

COPY --from=builder /usr/leadhit_test_task /usr/leadhit_test_task
COPY . ./

ENV PATH="/usr/leadhit_test_task/.venv/bin:$PATH"
ENV PYTHONPATH "${PYTHONPATH}:/usr/leadhit_test_task"

CMD ["uvicorn", "asgi:app", "--host", "0.0.0.0", "--port", "8080" ]
