from django.conf import settings


def session_settings(request):
    """
    Context processor to make session timeout settings available in templates.
    """
    return {
        "settings": {
            "SESSION_COOKIE_AGE": getattr(settings, "SESSION_COOKIE_AGE", 1800),
            "SESSION_TIMEOUT_WARNING": getattr(
                settings, "SESSION_TIMEOUT_WARNING", 300
            ),
        }
    }
