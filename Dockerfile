FROM python:3.9.5-slim

RUN pip install poetry

WORKDIR /server

COPY ./pyproject.toml .
COPY ./poetry.lock .

RUN poetry config virtualenvs.create false && poetry install

COPY server.py .
COPY curency_pb2.py .
COPY curency_twirp.py .
