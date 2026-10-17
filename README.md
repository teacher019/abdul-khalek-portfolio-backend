# Abdul Khalek Portfolio Backend

Django REST Framework-based backend for the Abdul Khalek Portfolio website.

## Features

- REST API for portfolio projects
- Project title, category, description, technologies and GitHub URL
- JSON responses
- Django database migrations
- CORS configuration for frontend integration

## Technology Stack

- Python
- Django
- Django REST Framework
- SQLite for local development
- Render for deployment

## Live API

**Projects API:**  
https://abdul-khalek-portfolio-backend.onrender.com/api/projects/

### API Endpoint

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/projects/` | Retrieve portfolio projects |

The projects endpoint returns JSON data containing project information.

## Local Installation

### 1. Clone the repository

```bash
git clone https://github.com/teacher019/abdul-khalek-portfolio-backend.git
cd abdul-khalek-portfolio-backend
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Apply database migrations

```powershell
python manage.py migrate
```

### 5. Start the development server

```powershell
python manage.py runserver
```

Open the local API:

http://127.0.0.1:8000/api/projects/

## API Testing

The projects endpoint can be tested using a browser, curl or Postman.

Example:

```bash
curl https://abdul-khalek-portfolio-backend.onrender.com/api/projects/
```

Expected result: HTTP 200 OK with a JSON array of portfolio projects.

## Deployment

The backend is deployed on Render. The repository includes a `build.sh` script for dependency installation, static file collection and database migrations.

## Repository

https://github.com/teacher019/abdul-khalek-portfolio-backend
## Postman API Testing

A Postman collection is included in the `submission/` directory for testing the Portfolio API.

**Collection file:** `submission/Abdul Khalek Portfolio API.postman_collection.json`

### How to test
1. Open Postman.
2. Click **Import**.
3. Select the Postman collection JSON file from the `submission/` directory.
4. Send the `GET` request to `https://abdul-khalek-portfolio-backend.onrender.com/api/projects/`.
5. Verify that the response status is `200 OK` and the response body contains JSON project data.
