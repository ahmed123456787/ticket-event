#!/bin/sh

set -e

# Function to wait for PostgreSQL to be ready
wait_for_postgres() {
  echo "Waiting for PostgreSQL to be ready..."
  while ! python -c "import psycopg2; psycopg2.connect(dbname='event_ticket', user='postgres', password='postgres', host='db')" 2>/dev/null; do
    echo "PostgreSQL not ready yet - sleeping 1s"
    sleep 1
  done
  echo "PostgreSQL is ready!"
}

# Function to wait for Redis to be ready
wait_for_redis() {
  echo "Waiting for Redis to be ready..."
  while ! python -c "import redis; r = redis.Redis(host='redis', port=6379); r.ping()" 2>/dev/null; do
    echo "Redis not ready yet - sleeping 1s"
    sleep 1
  done
  echo "Redis is ready!"
}

# Wait for services to be fully ready
wait_for_postgres
wait_for_redis

echo "Collecting static files..."
python manage.py collectstatic --noinput

python manage.py makemigrations core --empty


echo "Applying database migrations..."
python manage.py migrate --noinput


echo "Starting server..."
exec python manage.py runserver 0.0.0.0:8000