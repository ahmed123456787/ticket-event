FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install dependencies and curl for healthchecks
RUN apk add --no-cache curl

# Install dependencies
COPY requirements/production.txt requirements/production.txt
COPY requirements/base.txt requirements/base.txt
RUN pip install --no-cache-dir -r requirements/production.txt

# Copy entrypoint script
COPY deployment/entrypoint.sh /app/deployment/entrypoint.sh

# Fix permissions issue with explicit mode
RUN chmod +x /app/deployment/entrypoint.sh

# Copy project
COPY . /app/

# Ensure entrypoint is executable again after copying all files
RUN chmod +x /app/deployment/entrypoint.sh

# Expose port
EXPOSE 8000

# Run startup script
ENTRYPOINT ["/app/deployment/entrypoint.sh"]

