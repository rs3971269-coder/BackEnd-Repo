# Sample Server

A collection of small FastAPI and SQLAlchemy examples. The main application is a student management API in `main4.py`; the other `main*.py` files are separate learning examples covering tasks, books, request validation, feedback, background tasks, file uploads, and database operations.

## Student API

The student API is defined in `main4.py` and uses SQLAlchemy models from `model.py`, database setup from `database.py`, and request/response schemas from `schemas.py`. It creates the database tables when the application starts.

| Method | Endpoint | Description |
| --- | --- | --- |
| `POST` | `/student` | Create a student from a name and email |
| `GET` | `/student` | List students |
| `GET` | `/student/{student_id}` | Get one student by ID |

Interactive API documentation is available at `/docs` while the server is running.

> **Note:** The current SQLAlchemy student model requires an `address`, but the create route and request schema only provide `name` and `email`. Align these before relying on student creation.

## Requirements

- Python 3.10 or newer
- FastAPI
- Uvicorn
- SQLAlchemy
- `python-dotenv`
- A database driver supported by the SQLAlchemy URL you configure

There is no dependency manifest in this folder. Install the packages above and the driver required for your database before running the app.

## Configuration

The database connection is read from the `DATABASE_CONNECTION_URL` environment variable. The project loads values from a `.env` file in the working directory, so create or update `.env` with a URL appropriate for your database:

```env
DATABASE_CONNECTION_URL=your-sqlalchemy-database-url
```

Do not commit `.env` or put credentials in source control.

## Run the student API

From this folder, activate your virtual environment if you have one, then start the application:

```powershell
.\venv\Scripts\Activate.ps1
uvicorn main4:app --reload
```

If you are not using the included virtual environment, run the `uvicorn` command from an environment where the required packages and database driver are installed. By default, Uvicorn serves the API at `http://127.0.0.1:8000`.

## Other examples

The other Python files are standalone exercises, each defining its own FastAPI `app` or demonstrating direct database access:

- `main.py` — in-memory task and book endpoints
- `main2.py` — student query validation and feedback response models
- `main2sql.py` — SQLAlchemy department and employee models
- `main3.py` — background tasks and file upload/download examples
- `main4.py` — student management API
- `mainsql.py` — direct SQLAlchemy student queries and updates
- `database.py`, `model.py`, `schemas.py` — database connection, student model, and API schemas
- `upload/` — uploaded files and a note about CSS layout concepts

To run a different FastAPI example, replace `main4` in the Uvicorn command with that file's module name, such as `uvicorn main:app --reload`.
