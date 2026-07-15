# Task API

A simple RESTful CRUD API built using FastAPI for managing tasks. This project demonstrates core backend concepts such as Create, Read, Update, and Delete (CRUD) operations using in-memory storage.

## Features

- Create new tasks
- View all tasks
- View a specific task by ID
- Update existing tasks
- Delete tasks
- Input validation using Pydantic
- Interactive Swagger UI documentation
- Health check endpoint

---

## Tech Stack

- Python 3
- FastAPI
- Uvicorn
- Pydantic
- Swagger UI

---

## Project Structure

```text
task-api/
│
├── app/
│   ├── data/
│   │   └── task_store.py
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
│   ├── utils/
│   │
│   ├── __init__.py
│   └── main.py
│
├── tests/
│
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/task-api.git
cd task-api
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python run.py
```

Server starts at:

```text
http://127.0.0.1:8000
```

---

## Swagger Documentation

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Root endpoint |
| GET | /health | Health check |
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get task by ID |
| POST | /tasks | Create a task |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

---

## Example Request

### Create Task

Request Body:

```json
{
  "title": "Learn Docker"
}
```

Response:

```json
{
  "id": 4,
  "title": "Learn Docker",
  "done": false
}
```

---

## Example cURL Command

```bash
curl -X POST "http://127.0.0.1:8000/tasks" \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn Docker"}'
```

---

## Validation

Task titles must:

- be required
- have at least 1 character
- be at most 100 characters

---

## Status Codes

| Status Code | Meaning |
|------------|---------|
| 200 | Success |
| 201 | Resource Created |
| 204 | Resource Deleted |
| 404 | Resource Not Found |
| 422 | Validation Error |

---

## In-Memory Storage

This application currently stores data in memory using a Python list.

Any tasks created during runtime will be lost when the server restarts. This is intentional for the assignment and demonstrates the difference between in-memory storage and persistent databases.

---

## Future Improvements

- PostgreSQL integration
- SQLAlchemy ORM
- User authentication
- Docker support
- Unit testing
- Deployment to cloud

---

## Author

Srinidhi M D

Backend Development Internship Assignment

Built using FastAPI and Python.
