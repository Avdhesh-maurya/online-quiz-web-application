from mainapp.models import Question


def add_questions():
    Question.objects.create(
        text="Which of the following is the default database used by Django?",
        option1="PostgreSQL",
        option2="MySQL",
        option3="SQLite",
        option4="Oracle",
        answer="SQLite",
        category="Django",
    )

    Question.objects.create(
        text="What does the 'makemigrations' command do in Django?",
        option1="Applies migrations to the database",
        option2="Creates migration files based on model changes",
        option3="Deletes old migrations",
        option4="Starts the Django development server",
        answer="Creates migration files based on model changes",
        category="Django",
    )

    Question.objects.create(
        text="Which design pattern is Django based on?",
        option1="MVC (Model View Controller)",
        option2="MVT (Model View Template)",
        option3="MVVM (Model View ViewModel)",
        option4="None of the above",
        answer="MVT (Model View Template)",
        category="Django",
    )

    Question.objects.create(
        text="What file is used to configure database settings in Django?",
        option1="urls.py",
        option2="models.py",
        option3="settings.py",
        option4="apps.py",
        answer="settings.py",
        category="Django",
    )

    Question.objects.create(
        text="Which of these commands starts the Django development server?",
        option1="python manage.py runserver",
        option2="python manage.py startapp",
        option3="django-admin run",
        option4="python manage.py createsuperuser",
        answer="python manage.py runserver",
        category="Django",
    )

    print("✅ Django Quiz Questions added successfully!")
