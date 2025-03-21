from django.conf import settings


def expose_settings(request):
    return {
        "METABASE_BASE_URL": settings.METABASE_BASE_URL,
    }
