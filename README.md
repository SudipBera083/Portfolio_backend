## Django Core Backend

This is a simple Django 5 backend project named `core`, with two main apps: `contact` and `chatbot`. It exposes APIs that you can integrate with a frontend portfolio or other clients.

### Tech Stack

- **Framework**: Django 5
- **Language**: Python 3
- **Database**: SQLite (default, local development)

### Project Structure

- **`manage.py`**: Main Django management script.
- **`core/`**: Project configuration (settings, URLs, WSGI/ASGI).
- **`contact/`**: App for contact-related models, views, serializers, and URLs.
- **`chatbot/`**: App for chatbot-related models, views, services, and URLs.

### Getting Started

1. **Create and activate a virtual environment** (recommended):

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

2. **Install dependencies** (create and adjust `requirements.txt` as needed):

```bash
pip install django djangorestframework django-cors-headers
```

3. **Apply database migrations**:

```bash
python manage.py migrate
```

4. **Run the development server**:

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/` by default.

### Environment & Settings

- **Debug**: Currently `DEBUG = True` in `core/settings.py` (development only).
- **Database**: Uses local `db.sqlite3` at the project root.
- **CORS**: `CORS_ALLOW_ALL_ORIGINS = True` (relax this for production).

For production:

- Set a secure `SECRET_KEY` via environment variables.
- Set `DEBUG = False`.
- Configure `ALLOWED_HOSTS`.
- Switch to a production-ready database (e.g., PostgreSQL).

### Useful Commands

- **Run tests**:

```bash
python manage.py test
```

- **Create a superuser**:

```bash
python manage.py createsuperuser
```

### License

You can add your preferred license information here.

