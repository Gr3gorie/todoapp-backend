from fastapi import FastAPI
from src.database import engine, Base
from src.routers import users, notes

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TodoApp Backend",
    description="A simple FastAPI backend for managing users and notes.",
    version="1.0.0"
)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(notes.router, prefix="/notes", tags=["Notes"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the TodoApp Backend!"}
