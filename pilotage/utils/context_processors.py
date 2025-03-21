from django.conf import settings


def expose_settings(request):
    return {
        "EMPLOIS_BASE_URL": settings.EMPLOIS_BASE_URL,
        "GIP_SITE_BASE_URL": settings.GIP_SITE_BASE_URL,
        "HELP_CENTER_BASE_URL": settings.HELP_CENTER_BASE_URL,
        "MATOMO_BASE_URL": settings.MATOMO_BASE_URL,
        "MATOMO_SITE_ID": settings.MATOMO_SITE_ID,
        "METABASE_BASE_URL": settings.METABASE_BASE_URL,
    }
