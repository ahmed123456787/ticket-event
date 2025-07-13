#!/bin/sh

set -e

# Function to wait for PostgreSQL to be ready
wait_for_postgres() {
  echo "Waiting for PostgreSQL to be ready..."
  while ! python -c "import psycopg2; import os; psycopg2.connect(dbname=os.environ.get('DB_NAME', 'event_ticket'), user=os.environ.get('DB_USER', 'postgres'), password=os.environ.get('DB_PASSWORD', ''), host=os.environ.get('DB_HOST', 'db'))" 2>/dev/null; do
    echo "PostgreSQL not ready yet - sleeping 1s"
    sleep 1
  done
  echo "PostgreSQL is ready!"
}

# Function to wait for Redis to be ready
wait_for_redis() {
  echo "Waiting for Redis to be ready..."
  while ! python -c "import redis; import os; r = redis.Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=int(os.environ.get('REDIS_PORT', 6379))); r.ping()" 2>/dev/null; do
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

python manage.py makemigrations 

python manage.py showmigrations core

# Finally apply all other migrations
python manage.py migrate 

echo "Starting server..."
exec python manage.py runserver 0.0.0.0:8000