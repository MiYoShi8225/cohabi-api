FROM python:3.9-alpine

WORKDIR /app

COPY docker/requirements.txt docker/requirements.txt

RUN set -eux \
    && apk update \
    && apk add --no-cache \
    build-base \
    gcc \
    mariadb-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir --trusted-host pypi.python.org -r docker/requirements.txt \
    && apk del build-base

COPY . .
EXPOSE 8000
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]