# Build stage
FROM python:3.11-alpine as builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /build

# Install build dependencies
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    python3-dev

# Install dependencies
COPY requirements/production.txt requirements/production.txt
COPY requirements/base.txt requirements/base.txt
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /build/wheels -r requirements/production.txt

# Final stage
FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk add --no-cache curl

RUN adduser --disabled-password --no-create-home appuser

COPY --from=builder /build/wheels /wheels
RUN pip install --no-cache-dir --no-index --find-links=/wheels /wheels/* && \
    rm -rf /wheels

COPY deployment/entrypoint.sh /app/deployment/entrypoint.sh
RUN chmod +x /app/deployment/entrypoint.sh

COPY . /app/

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

ENTRYPOINT ["/app/deployment/entrypoint.sh"]

