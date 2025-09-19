import time
from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import JsonResponse
from django.urls import reverse


class SessionTimeoutMiddleware:
    """
    Middleware to handle automatic session timeout and logout.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if user is authenticated
        if request.user.is_authenticated:
            # Get current time
            current_time = time.time()

            # Get last activity time from session
            last_activity = request.session.get("last_activity")

            if last_activity:
                # Calculate time elapsed since last activity
                time_elapsed = current_time - last_activity

                # Check if session has expired
                session_timeout = getattr(settings, "SESSION_COOKIE_AGE", 1800)

                if time_elapsed > session_timeout:
                    # Session expired - logout user
                    logout(request)

                    # Check if it's an AJAX request
                    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                        return JsonResponse(
                            {
                                "session_expired": True,
                                "message": "Your session has expired. Please log in again.",
                                "redirect_url": reverse("login"),
                            },
                            status=401,
                        )

                    # For regular requests, redirect to login
                    return redirect("login")

            # Update last activity time
            request.session["last_activity"] = current_time

        response = self.get_response(request)
        return response
