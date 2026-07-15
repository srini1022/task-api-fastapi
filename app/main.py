from fastapi import FastAPI
from app.routes.tasks import router as task_router

app = FastAPI(
    title="Task API",
    description="A simple task management CRUD API",
    version="1.0.0"
)

app.include_router(task_router)

@app.get("/")
def root():
    return {
        "message": "Task API is running"
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }