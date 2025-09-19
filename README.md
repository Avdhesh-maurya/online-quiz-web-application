# Online Quiz Application

A Django-based quiz application with auto-logout session management and multiple quiz categories.

## Features

- User authentication (signup, login, logout)
- Auto-logout session management with warnings
- Multiple quiz categories (HTML, CSS, JavaScript, Java, Bootstrap, Node.js, Django)
- Leaderboard system
- Responsive design with Bootstrap
- Session timeout warnings with countdown

## Deployment on Render

### Prerequisites

1. GitHub account
2. Render account (render.com)

### Step 1: Prepare Repository

1. Create a new repository on GitHub
2. Copy only the `quizzapp` folder contents to your repository (not the root folder)
3. The repository structure should look like:

```
your-repo/
├── build.sh
├── requirements.txt
├── runtime.txt
├── .gitignore
├── .env.example
├── manage.py
├── db.sqlite3
├── quizzapp/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── mainapp/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── middleware.py
    ├── static/
    ├── templates/
    └── migrations/
```

### Step 2: Deploy on Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New" → "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: Your app name
   - **Environment**: Python 3
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn quizzapp.wsgi:application`
   - **Instance Type**: Free tier

### Step 3: Environment Variables

Add these environment variables in Render:

```
SECRET_KEY=your-very-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
PYTHON_VERSION=3.12.0
```

Optional (for admin user creation):
```
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=your-secure-password
```

### Step 4: Database

Render will automatically provide a PostgreSQL database. The `DATABASE_URL` environment variable will be set automatically.

### Step 5: Deploy

1. Click "Create Web Service"
2. Wait for the build to complete
3. Your app will be available at `https://your-app-name.onrender.com`

## Local Development

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and update values
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```
7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Session Timeout Configuration

The application includes automatic session timeout with the following default settings:
- Session timeout: 30 minutes
- Warning shown: 5 minutes before expiry
- Session extends on user activity

Configure in `settings.py`:
```python
SESSION_COOKIE_AGE = 1800  # 30 minutes
SESSION_TIMEOUT_WARNING = 300  # 5 minutes warning
```

## Adding Quiz Questions

Use the Django admin panel or run the question scripts:
```bash
python manage.py shell
exec(open('mainapp/add_html_questions.py').read())
exec(open('mainapp/add_css_questions.py').read())
# ... etc for other categories
```

## Support

For issues and questions, contact support through the application's FAQ section.