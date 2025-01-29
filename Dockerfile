FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ["./poetry.lock","./pyproject.toml", "/app/"]

RUN pip install --upgrade pip &&\
    pip install poetry &&\
    poetry config virtualenvs.create false

RUN poetry install --only main

COPY . /app

# Otworzenie portu
EXPOSE 8000

# Uruchomienie serwera
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
