FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /usr/src/dj_shop
COPY poetry.lock pyproject.toml /usr/src/dj_shop/
RUN pip install poetry
RUN poetry install --no-dev

COPY . /usr/src/dj_shop
RUN chmod +x /usr/src/dj_shop/docker-entrypoint.sh