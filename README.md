
# TodoApp Backend

## Prerequisites
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)
- **Poetry** (optional) : [Install Poetry](https://python-poetry.org/docs/)

---

## How to Run the Project Using Docker Compose

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gr3gorie/todoapp-backend.git
   cd todoapp-backend
   ```
2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. **Start Docker containers**:
   ```bash
   docker-compose up --build -d
   ```

4. **Verify that the containers are running**:
   ```bash
   docker ps
   ```
   There should be two containers:
   - `todoapp_postgres` (PostgreSQL database)
   - `todoapp_backend` (FastAPI backend)

5. Run the FastAPI server locally:
   ```bash
   uvicorn src.main:app --reload
   ```

6. Access the API at:  
   [http://localhost:8000](http://localhost:8000)

4. **Access the API documentation**:
   - **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
   - **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Database Access with pgAdmin

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

