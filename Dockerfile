# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Poetry lock and config files
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry

# Install the dependencies
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Copy the entire application code into the container
COPY . /app

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the application with Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
