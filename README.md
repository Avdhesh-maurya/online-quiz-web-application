# Online Quiz Application

A Django-based quiz application with auto-logout session management and multiple quiz categories.

## 🚀 Live Demo

**Access the live application:** [https://online-quiz-app-u9n8.onrender.com/](https://online-quiz-app-u9n8.onrender.com/)

## 📸 Screenshots

### Homepage
<img width="1820" height="980" alt="image" src="https://github.com/user-attachments/assets/b9427012-4044-4e19-905a-9bc49bd0fe4e" />
*Clean and modern homepage with quiz categories*

### Quiz Interface
<img width="1820" height="980" alt="image" src="https://github.com/user-attachments/assets/1dd3cfaa-c56c-4731-9988-1fdb6f4c36af" />
*Interactive quiz taking experience with modern UI*

### Leaderboard
<img width="1820" height="881" alt="image" src="https://github.com/user-attachments/assets/d5b38f99-de2b-4bf9-9bb5-828bd546d5a3" />
*Track your progress and compete with others*

### Mobile View
<img width="497" height="718" alt="image" src="https://github.com/user-attachments/assets/a9c07642-764e-4c53-8c84-955b4c9fafcf" />

*Fully responsive design works on all devices*

## ✨ Features

- 🔐 **User Authentication** - Secure signup, login, and logout system
- ⏰ **Auto-logout Session Management** - Smart session handling with warnings
- 📚 **Multiple Quiz Categories** - HTML, CSS, JavaScript, Python, Java, Bootstrap, Node.js, Django
- 🏆 **Leaderboard System** - Track scores and compete with others
- 📱 **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- ⚡ **Real-time Feedback** - Instant results and score calculation
- 🎯 **Session Timeout Warnings** - User-friendly countdown notifications
- 🎨 **Modern UI/UX** - Clean, intuitive interface with smooth animations

## 🛠️ Technology Stack

### Backend
- **Django** - Python web framework
- **SQLite** - Database for development
- **Python** - Programming language

### Frontend
- **Bootstrap 5** - CSS framework for responsive design
- **HTML5/CSS3** - Modern web standards
- **JavaScript** - Interactive user experience
- **Bootstrap Icons** - Beautiful icon set

### Deployment
- **Render** - Cloud hosting platform
- **Git** - Version control

## 📋 Installation & Setup

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/Avdhesh-maurya/online-quiz-web-application.git
cd online-quiz-web-application
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Create superuser (optional)**
```bash
python manage.py createsuperuser
```

6. **Start development server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the application.

## 🚀 Deployment on Render

### Prerequisites

1. GitHub account
2. Render account (render.com)

### Step 1: Prepare Repository

1. Create a new repository on GitHub
2. Copy only the `quizzapp` folder contents to your repository (not the root folder)

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

## 📱 Adding Quiz Questions

Use the Django admin panel or run the question scripts:
```bash
python manage.py shell
exec(open('mainapp/add_html_questions.py').read())
exec(open('mainapp/add_css_questions.py').read())
# ... etc for other categories
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Workflow
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Avdhesh Kumar**
- GitHub: [@Avdhesh-maurya](https://github.com/Avdhesh-maurya)
- Twitter: [@Avdhesh_kumar08](https://twitter.com/Avdhesh_kumar08)
- LinkedIn: [avdhesh-kumar07](https://linkedin.com/in/avdhesh-kumar07)

## 🙏 Acknowledgments

- Built with [Django](https://djangoproject.com/)
- Styled with [Bootstrap 5](https://getbootstrap.com/)
- Icons by [Bootstrap Icons](https://icons.getbootstrap.com/)
- Deployed on [Render](https://render.com/)

## 📞 Support

For issues and questions, contact support through the application's FAQ section or create an issue on GitHub.

---

⭐ **Star this repository if you found it helpful!**
