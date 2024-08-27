# Use the latest Ubuntu image
FROM ubuntu:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies and PostgreSQL client tools
RUN apt-get update && \
    apt-get install -y \
    python3-pip \
    python3-dev \
    python3-venv \
    build-essential \
    wget \
    gnupg \
    lsb-release \
    mariadb-client \
    && rm -rf /var/lib/apt/lists/*

# Install PostgreSQL client tools for version 16
RUN apt-get update && \
    apt-get install -y \
    postgresql-client-16 \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python3 -m venv /env

# Upgrade pip in the virtual environment
RUN /env/bin/pip install --upgrade pip

# Copy and install Python dependencies
COPY requirements.txt /app/
RUN /env/bin/pip install --no-cache-dir -r /app/requirements.txt

# Copy the Django project files into the container
COPY . /app/

# Set environment variables to use the virtual environment
ENV PATH="/env/bin:$PATH"

# Run Django management commands
RUN /env/bin/python manage.py collectstatic --noinput
RUN /env/bin/python manage.py migrate --noinput

# Expose port 8000 for the Django application
EXPOSE 8000

# Run the Django application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "db_manager.wsgi:application"]