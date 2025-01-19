# Base image
FROM quay.io/astronomer/astro-runtime:12.6.0

# Set environment variables
ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"

# Switch to root user to install system dependencies
USER root

# Install Poetry dependencies
RUN apt-get update && apt-get install -y curl python3-distutils \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Copy project files
WORKDIR /usr/local/airflow
COPY . .

# Install Python dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-root