# Base image with Python 3.10.13
FROM python:3.10.13-slim

# Set environment variables to reduce Poetry noise
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.8.2

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential gcc git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Create app directory
WORKDIR /app

# Copy only the dependency files first for layer caching
COPY pyproject.toml poetry.lock* /app/

# Install dependencies (without virtualenv)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of your application code
COPY . /app

# Expose port for FastAPI/Flask if needed
EXPOSE 8000

# Default command (adjust if using Flask or uvicorn)
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
