from django.conf import settings


def expose_settings(request):
    return {
        "HELP_CENTER_BASE_URL": settings.HELP_CENTER_BASE_URL,
        "METABASE_BASE_URL": settings.METABASE_BASE_URL,
    }
