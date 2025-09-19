# ---------------- FAQ Pages ----------------
def faq_how_to_play(request):
    return render(request, "faq_how_to_play.html")


def faq_scoring_rules(request):
    return render(request, "faq_scoring_rules.html")


def faq_contact_support(request):
    return render(request, "faq_contact_support.html")


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Leaderboard
from .models import Question
import random
import json

# ---------------- Quiz Page ----------------
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def quiz_view(request, category):
    print("DEBUG: category =", category)
    print(
        "DEBUG: Tailwind count =", Question.objects.filter(category="Tailwind").count()
    )
    questions = Question.objects.filter(category=category)
    print("DEBUG: questions for", category, "=", questions.count())
    # Remove duplicates by question text (keep the first occurrence)
    seen = set()
    unique_questions = []
    for q in questions:
        if q.text not in seen:
            unique_questions.append(q)
            seen.add(q.text)
    # Handle case when no questions exist for this category
    if not unique_questions:
        from django.contrib import messages

        messages.warning(request, f"No questions found for {category} yet!")
        return redirect("index")
    total = len(unique_questions)
    # Randomize questions
    random.shuffle(unique_questions)
    # Prepare questions with shuffled options
    question_data = []
    for q in unique_questions:
        options = [q.option1, q.option2, q.option3, q.option4]
        random.shuffle(options)
        question_data.append(
            {
                "id": q.id,
                "text": q.text,
                "options": options,
                "answer": q.answer,
            }
        )
    score = None
    if request.method == "POST":
        score = 0
        for q in unique_questions:
            selected = request.POST.get(f"q{q.id}", "").strip()
            if selected == str(q.answer).strip():
                score += 1
        Leaderboard.objects.filter(user=request.user, category=category).delete()
        Leaderboard.objects.update_or_create(
            user=request.user,
            category=category,
            defaults={"score": score, "total": total},
        )
    return render(
        request,
        "quiz.html",
        {
            "questions": question_data,
            "score": score,
            "total": total,
            "category": category,
        },
    )


# ---------------- Home Page ----------------
def home(request):
    return HttpResponse("Hello, Django running from CMD!")


# ---------------- Index Page ----------------
def index(request):
    frontend_data = [
        {
            "title": "HTML Quiz",
            "description": "Quick quiz to test your basics of HTML.",
            "image": "img/HTML-Quiz-3.webp",
            "link": "/quiz/HTML/",
        },
        {
            "title": "CSS Quiz",
            "description": "Test your knowledge of CSS selectors, layouts, and colors.",
            "image": "img/CSS-QUIZ-2.webp",
            "link": "/quiz/CSS/",
        },
        {
            "title": "JavaScript Quiz",
            "description": "Challenge your skills in JavaScript — variables, DOM, events.",
            "image": "img/Javascript quiz.jpg",
            "link": "/quiz/JavaScript/",
        },
        {
            "title": "React Quiz",
            "description": "Test your React knowledge — components, state, props.",
            "image": "img/react-quiz.png",
            "link": "/quiz/React/",
        },
        {
            "title": "Vue Quiz",
            "description": "Test your Vue.js knowledge — directives, components, reactivity.",
            "image": "img/vue.jpeg",
            "link": "/quiz/Vue/",
        },
        {
            "title": "Angular Quiz",
            "description": "Test your Angular knowledge — modules, components, services.",
            "image": "img/angularQuizz.jpeg",
            "link": "/quiz/Angular/",
        },
        {
            "title": "Bootstrap Quiz",
            "description": "Test your Bootstrap knowledge — grid, components, utilities.",
            "image": "img/bootstrap.jpeg",
            "link": "/quiz/Bootstrap/",
        },
        {
            "title": "Tailwind CSS Quiz",
            "description": "Test your Tailwind CSS knowledge — utility classes, responsive design.",
            "image": "img/tailwind.png",
            "link": "/quiz/Tailwind/",
        },
    ]

    backend_data = [
        {
            "title": "Python Quiz",
            "description": "Practice Python basics, OOP, and frameworks.",
            "image": "img/python.png",
            "link": "/quiz/Python/",
        },
        {
            "title": "Django Quiz",
            "description": "Practice Django basics, MVT structure, and frameworks.",
            "image": "img/jango.jpg",
            "link": "/quiz/Django/",
        },
        {
            "title": "Java Quiz",
            "description": "Test your knowledge of Java basics, OOP, and frameworks.",
            "image": "img/java-quiz.jpg",
            "link": "/quiz/Java/",
        },
        {
            "title": "Node.js Quiz",
            "description": "Test your knowledge of Node.js basics, modules, and frameworks.",
            "image": "img/nodejs.png",
            "link": "/quiz/Node.js/",
        },
        {
            "title": "Express.js Quiz",
            "description": "Test your knowledge of Express.js routing, middleware, and APIs.",
            "image": "img/expressjs.png",
            "link": "/quiz/Express.js/",
        },
        {
            "title": "PHP Quiz",
            "description": "Test your knowledge of PHP basics, web development, and frameworks.",
            "image": "img/php.jpg",
            "link": "/quiz/PHP/",
        },
    ]

    return render(
        request,
        "index.html",
        {"frontend_data": frontend_data, "backend_data": backend_data},
    )


# ---------------- Leaderboard Page ----------------


@login_required(login_url="login")
def leaderboard_view(request):
    scores = Leaderboard.objects.order_by("-score", "date")[:20]  # top 20
    return render(request, "leaderboard.html", {"scores": scores})


# ---------------- JSON Data for HTML Quiz (Optional for JS-based quiz) ----------------
def html_quiz(request):
    questions = Question.objects.filter(category="HTML")
    question_list = []
    for q in questions:
        question_list.append(
            {
                "id": q.id,
                "question": q.text,
                "options": [q.option1, q.option2, q.option3, q.option4],
                "answer": q.answer,
            }
        )
    return render(
        request, "html_quiz.html", {"questions_json": json.dumps(question_list)}
    )


# ---------------- Signup ----------------
def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("login")
    return render(request, "signup.html")


# ---------------- Login ----------------
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Initialize session timeout tracking
            request.session["last_activity"] = time.time()
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")


#
# ---------------- Logout ----------------
def logout_view(request):
    """Log out the user and redirect to the home page."""
    logout(request)
    return redirect("index")


# ---------------- Session Management ----------------
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import time


@login_required
@require_http_methods(["POST"])
def extend_session_view(request):
    """Extend user session by updating last activity time."""
    try:
        # Update last activity time in session
        request.session["last_activity"] = time.time()

        return JsonResponse(
            {"success": True, "message": "Session extended successfully"}
        )
    except Exception as e:
        return JsonResponse(
            {"success": False, "message": "Failed to extend session"}, status=500
        )


@login_required
@require_http_methods(["GET"])
def check_session_view(request):
    """Check if user session is still valid."""
    try:
        # If we reach here, the middleware has already validated the session
        return JsonResponse({"success": True, "authenticated": True})
    except Exception as e:
        return JsonResponse({"success": False, "authenticated": False}, status=500)
