from django.conf import settings


def expose_settings(request):
    return {
        "HELP_CENTER_BASE_URL": settings.HELP_CENTER_BASE_URL,
        "MATOMO_BASE_URL": settings.MATOMO_BASE_URL,
        "MATOMO_SITE_ID": settings.MATOMO_SITE_ID,
        "METABASE_BASE_URL": settings.METABASE_BASE_URL,
    }
