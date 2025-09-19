from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),  # Django admin panel
    path("", views.index, name="index"),  # Home/index
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    # Session management
    path("extend-session/", views.extend_session_view, name="extend_session"),
    path("check-session/", views.check_session_view, name="check_session"),
    # Quiz routes
    path("quiz/<str:category>/", views.quiz_view, name="quiz"),
    path("html_quiz/", views.html_quiz, name="html_quiz"),
    path(
        "leaderboard/", views.leaderboard_view, name="leaderboard"
    ),  # Leaderboard view
    # FAQ pages
    path("faq/how-to-play/", views.faq_how_to_play, name="faq_how_to_play"),
    path("faq/scoring-rules/", views.faq_scoring_rules, name="faq_scoring_rules"),
    path("faq/contact-support/", views.faq_contact_support, name="faq_contact_support"),
]
