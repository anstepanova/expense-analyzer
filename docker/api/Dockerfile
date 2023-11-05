FROM python:3.12.0-alpine3.18 AS base

WORKDIR /usr/src/server

RUN apk update && apk add gcc libc-dev libffi-dev openssl-dev python3-dev g++ postgresql-dev musl-dev

RUN pip install --upgrade pip

RUN pip install -U poetry

COPY ./expense_analyzer ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]