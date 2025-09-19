# Deployment Guide for Your Repository

## Repository Structure for Render Deployment

Your repository at `https://github.com/Avdhesh-maurya/online-quiz-web-application.git` should have this structure in the root:

```
online-quiz-web-application/
├── build.sh
├── requirements.txt
├── runtime.txt
├── .gitignore
├── .env.example
├── README.md
├── Procfile
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

## Steps to Deploy on Render

### 1. Update Your GitHub Repository

Copy the contents of your `quizzapp` folder to the root of your repository:

```bash
# Navigate to your local repository
cd path/to/your/local/repo

# Copy all files from quizzapp folder to root (excluding the quizzapp folder itself)
# Make sure these files are in the ROOT of your repository:
- build.sh
- requirements.txt
- runtime.txt
- .gitignore
- .env.example
- README.md
- Procfile
- manage.py
- db.sqlite3
- quizzapp/ (Django project folder)
- mainapp/ (Django app folder)
```

### 2. Commit and Push Changes

```bash
git add .
git commit -m "Prepare for Render deployment with auto-logout session"
git push origin main
```

### 3. Deploy on Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New" → "Web Service"
3. Connect your GitHub account and select: `Avdhesh-maurya/online-quiz-web-application`
4. Configure the service:
   - **Name**: `online-quiz-app` (or your preferred name)
   - **Environment**: `Python 3`
   - **Branch**: `main`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn quizzapp.wsgi:application`
   - **Instance Type**: `Free`

### 4. Environment Variables

Add these environment variables in Render dashboard:

**Required:**
```
SECRET_KEY=django-insecure-your-new-secret-key-change-this-for-production
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
```

**Optional (for admin user creation):**
```
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@yourdomain.com
DJANGO_SUPERUSER_PASSWORD=YourSecurePassword123!
```

### 5. Database Configuration

Render will automatically provide a PostgreSQL database and set the `DATABASE_URL` environment variable. Your app is configured to use it automatically.

### 6. Deploy

1. Click "Create Web Service"
2. Wait for the build process to complete (5-10 minutes)
3. Your app will be available at: `https://your-app-name.onrender.com`

## Features Included

✅ **Auto-logout session management**
- 30-minute session timeout
- 5-minute warning before logout
- Client-side countdown timer
- Automatic session extension on activity

✅ **Production-ready configuration**
- Environment variables
- PostgreSQL database support
- Static file serving with WhiteNoise
- Security headers
- HTTPS redirect in production

✅ **Quiz application features**
- User authentication
- Multiple quiz categories
- Leaderboard system
- Responsive design

## Post-Deployment

1. **Access your app**: `https://your-app-name.onrender.com`
2. **Admin panel**: `https://your-app-name.onrender.com/admin/`
3. **Add quiz questions** through admin panel or Django shell

## Troubleshooting

If deployment fails:
1. Check Render build logs
2. Ensure all files are in repository root
3. Verify environment variables are set
4. Check that `build.sh` has execute permissions

## Local Development

To run locally:
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Your app will be available at: `http://127.0.0.1:8000`