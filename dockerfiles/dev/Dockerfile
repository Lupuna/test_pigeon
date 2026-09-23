FROM python:3.14-alpine3.23

WORKDIR /app

ENV PYTHONPATH=/app/src \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt /app/requirements.txt

RUN apk add --no-cache --virtual .build-deps build-base \
    && pip install --no-cache-dir -r /app/requirements.txt \
    && apk del .build-deps

COPY src /app/src

WORKDIR /app/src

EXPOSE 8000
