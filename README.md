
# TodoApp Backend

## Prerequisites
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)
- **Poetry** (optional) : [Install Poetry](https://python-poetry.org/docs/)

---

## How to Run the Project Using Docker Compose

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/todoapp-backend.git
   cd todoapp-backend
   ```

2. **Start Docker Containers**:
   Use the following command to **build and start** the PostgreSQL and FastAPI containers:
   ```bash
   docker-compose up --build -d
   ```

3. **Verify that the Containers Are Running**:
   ```bash
   docker ps
   ```
   You should see two containers:
   - `todoapp_postgres` (PostgreSQL database)
   - `todoapp_backend` (FastAPI backend)


4. **Access the API Documentation**:
   Open your browser and go to:
   - **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
   - **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Environment Variables

The following **environment variables** are used in the project. Make sure they are correctly configured in the **`docker-compose.yml`** file:

```yaml
POSTGRES_USER: user
POSTGRES_PASSWORD: password
POSTGRES_DB: todoapp_db
DATABASE_URL: postgresql://user:password@db:5432/todoapp_db
SECRET_KEY: your-secret-key
ALGORITHM: HS256
ACCESS_TOKEN_EXPIRE_MINUTES: 30
```

---

## Database Access with pgAdmin (Optional)

1. Open **pgAdmin** and **register a new server**.
2. Use the following details to connect:
   - **Host**: `localhost` (or the container's IP)
   - **Port**: `6666` (or the port you configured)
   - **Username**: `user`
   - **Password**: `password`
   - **Database**: `todoapp_db`

---

## Stopping the Containers

To **stop the containers**, run:

```bash
docker-compose down
```

---

## Local Development (Optional)

If you want to develop locally, follow these steps:

1. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

2. Run the FastAPI server locally:
   ```bash
   uvicorn src.main:app --reload
   ```

3. Access the API at:  
   [http://localhost:8000](http://localhost:8000)

