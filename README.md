# Task API

A RESTful CRUD API built using FastAPI and PostgreSQL for managing tasks.

This project demonstrates:

- FastAPI REST APIs
- CRUD Operations
- Repository Pattern
- PostgreSQL Integration
- Docker & Docker Compose
- Environment Variables
- Persistent Storage using Docker Volumes

---

# Features

- Create new tasks
- View all tasks
- View a task by ID
- Update tasks
- Delete tasks
- PostgreSQL persistent storage
- Dockerized database
- Interactive Swagger documentation
- Repository pattern architecture

---

# Tech Stack

- Python 3
- FastAPI
- PostgreSQL
- Docker
- Docker Compose
- Psycopg2
- Python Dotenv
- Uvicorn
- Pydantic

---

# Project Structure

```text
task-api/
│
├── app/
│   ├── data/
│   │
│   ├── repositories/
│   │   ├── memory_repository.py
│   │   └── postgres_repository.py
│   │
│   ├── routes/
│   │   └── tasks.py
│   │
│   ├── schemas/
│   │   └── task.py
│   │
│   ├── services/
│   │   └── task_service.py
│   │
│   ├── database.py
│   ├── main.py
│   └── __init__.py
│
├── .env.example
├── .gitignore
├── docker-compose.yml
├── README.md
├── requirements.txt
├── run.py
│
└── tests/
```

---

# Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:postgres@127.0.0.1:5432/taskdb
```

A sample configuration is provided in:

```text
.env.example
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/task-api.git
cd task-api
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

# Docker Setup

Start PostgreSQL:

```bash
docker compose up -d
```

Verify container:

```bash
docker ps
```

Expected container:

```text
task-db
```

Stop containers:

```bash
docker compose down
```

---

# Running the Application

Start FastAPI:

```bash
python run.py
```

Application:

```text
http://127.0.0.1:8000
```

---

# Swagger Documentation

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | / | Root Endpoint |
| GET | /health | Health Check |
| GET | /tasks | Get All Tasks |
| GET | /tasks/{id} | Get Task By ID |
| POST | /tasks | Create Task |
| PUT | /tasks/{id} | Update Task |
| DELETE | /tasks/{id} | Delete Task |

---

# Example Request

## Create Task

Request:

```json
{
  "title": "Learn Docker"
}
```

Response:

```json
{
  "id": 1,
  "title": "Learn Docker",
  "done": false
}
```

---

# Repository Pattern

The application follows the Repository Pattern.

Two repositories exist:

### Memory Repository

```text
memory_repository.py
```

Used in the initial version.

### PostgreSQL Repository

```text
postgres_repository.py
```

Used in the current implementation.

The service layer remains unchanged while storage implementation can be swapped.

Architecture:

```text
Routes
  ↓
Services
  ↓
Repositories
  ↓
Database
```

This demonstrates separation of concerns and maintainable backend architecture.

---

# PostgreSQL Integration

Tasks are stored inside PostgreSQL.

Database:

```text
taskdb
```

Table:

```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    done BOOLEAN DEFAULT FALSE
);
```

---

# Persistence Proof

To verify persistence:

### Step 1

Created a task:

```json
{
  "title": "Persistence Test"
}
```

### Step 2

Verified task exists using:

```http
GET /tasks
```

### Step 3

Restarted PostgreSQL container:

```bash
docker compose down
docker compose up -d
```

### Step 4

Executed:

```http
GET /tasks
```

Result:

The task was still present after restart.

This confirms PostgreSQL data persistence.

---

# Docker Volume

Data is persisted using:

```yaml
volumes:
  postgres_data:
```

Mounted as:

```yaml
postgres_data:/var/lib/postgresql/data
```

Therefore data survives:

- Application restarts
- Container restarts
- Docker compose down/up cycles

---

# Status Codes

| Status Code | Meaning |
|------------|---------|
| 200 | Success |
| 201 | Created |
| 204 | Deleted |
| 404 | Not Found |
| 422 | Validation Error |

---

# Future Improvements

- SQLAlchemy ORM
- Alembic Database Migrations
- User Authentication
- JWT Authorization
- Unit Testing
- CI/CD Pipeline
- Cloud Deployment

---

# Author

**Srinidhi M D**

Backend Development Internship Assignment

Built using FastAPI, PostgreSQL, Docker, and Python.
