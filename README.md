# Abdul Khalek Portfolio Backend

Django REST Framework API for a personal portfolio and blog website.

## Technology Stack

- Python
- Django
- Django REST Framework
- SQLite for local development
- Render deployment
- django-cors-headers
- WhiteNoise for static files

## Features

- Profile and portfolio project APIs
- Published blog list and detail APIs
- Blog search and category filtering
- Visitor comments with moderation
- Django Admin management for projects, posts and comments
- CORS configuration for the deployed React frontend

## Live URLs

- Backend base: https://abdul-khalek-portfolio-backend.onrender.com
- Profile: https://abdul-khalek-portfolio-backend.onrender.com/api/profile/
- Projects: https://abdul-khalek-portfolio-backend.onrender.com/api/projects/
- Blog: https://abdul-khalek-portfolio-backend.onrender.com/api/blog/
- Django Admin: https://abdul-khalek-portfolio-backend.onrender.com/admin/
- Frontend: https://abdul-khalek-portfolio-frontend.vercel.app/
- Frontend repository: https://github.com/teacher019/abdul-khalek-portfolio-frontend
- Backend repository: https://github.com/teacher019/abdul-khalek-portfolio-backend

## API Endpoint Reference

All API endpoints below are public and do not require API authentication in the current view implementation.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/profile/` | Retrieve profile information |
| GET | `/api/projects/` | Retrieve all projects |
| GET | `/api/projects/<id>/` | Retrieve one project |
| GET | `/api/blog/` | Retrieve published blog posts |
| GET | `/api/blog/?search=web` | Search published posts by title, excerpt or content |
| GET | `/api/blog/?category=Web%20Development` | Filter published posts by category |
| GET | `/api/blog/<slug>/` | Retrieve one published blog post |
| GET | `/api/blog/<slug>/comments/` | Retrieve approved comments for a published post |
| POST | `/api/blog/<slug>/comments/` | Submit a comment for moderation |

### Comment submission example

Send JSON to `POST /api/blog/<slug>/comments/`:

```json
{
  "name": "Demo Visitor",
  "email": "visitor@example.com",
  "message": "This is a test comment."
}
```

A valid comment returns HTTP 201 and remains pending until approved in Django Admin. Invalid data returns HTTP 400.

## Models and Relationships

- **Project**: title, category, description, technologies (JSON), GitHub URL and creation timestamp.
- **BlogPost**: title, unique slug, category, excerpt, content, published status, creation timestamp and update timestamp.
- **BlogComment**: foreign key to BlogPost, visitor name, email, message, approval status and creation timestamp.

Relationship: one BlogPost can have many BlogComment records. Deleting a post also deletes its related comments (`on_delete=CASCADE`).

## Permissions and Throttling

The API views use Django REST Framework `@api_view` decorators and do not define custom permission or throttle classes. No explicit project-level `DEFAULT_PERMISSION_CLASSES`, `DEFAULT_THROTTLE_CLASSES` or `DEFAULT_THROTTLE_RATES` configuration was found in the current settings. Django Admin is a separate authenticated management interface.

## Environment Variables

Set environment variables in your local environment or deployment dashboard. Never commit `.env` or production secrets.

| Variable | Purpose | Example |
|---|---|---|
| `DJANGO_SECRET_KEY` | Django secret key | `replace-with-a-new-secret-key` |
| `DJANGO_DEBUG` | Enables debug mode when set to `True` | `True` |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated allowed hostnames | `127.0.0.1,localhost` |
| `CORS_ALLOWED_ORIGINS` | Allowed frontend origins for CORS | `http://localhost:5173,http://127.0.0.1:5173` |
| `DATABASE_URL` | Optional database URL read by `dj_database_url`; SQLite is the default | Deployment-specific |

The project reads these environment variables through `config/settings.py`. Create `.env` locally using `.env.example` as a reference, and configure production values in the deployment dashboard. Do not commit `.env` or real secrets.

## Local Setup

### 1. Clone

```powershell
git clone https://github.com/teacher019/abdul-khalek-portfolio-backend.git
cd abdul-khalek-portfolio-backend
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Configure environment

Create a local `.env` file using `.env.example` as a reference. Use a unique local secret key and appropriate local settings. Do not upload `.env`.

### 5. Apply migrations

```powershell
python manage.py migrate
```

### 6. Create an administrator

```powershell
python manage.py createsuperuser
```

### 7. Run the server

```powershell
python manage.py runserver
```

Visit `http://127.0.0.1:8000/api/projects/` and `http://127.0.0.1:8000/admin/`.

## Postman Collection

Import `submission/Abdul Khalek Portfolio API.postman_collection.json` into Postman. The collection contains requests for profile, projects, blog search/filter, post details and comment moderation endpoints.

Use the `baseUrl` and `postSlug` collection variables. Set `postSlug` to an existing published post's actual slug before testing detail or comment requests. Sending a POST comment request creates a pending comment.

## Deployment

The backend is deployed on Render. Review `build.sh`, `requirements.txt` and deployment environment variables when configuring another instance.

