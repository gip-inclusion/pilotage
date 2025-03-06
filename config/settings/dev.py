from config.settings.base import *  # noqa: F403


# Django settings
# ---------------
DEBUG = True

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False

SECURE_HSTS_INCLUDE_SUBDOMAINS = False

SECURE_SSL_REDIRECT = False

SECURE_HSTS_PRELOAD = False

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

AUTH_PASSWORD_VALIDATORS = []  # Avoid password strength validation in DEV.

SECRET_KEY = "foobar"

INSTALLED_APPS.extend(  # noqa: F405
    [
        "debug_toolbar",
    ]
)

INTERNAL_IPS = ["127.0.0.1"]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405

DATABASES["default"]["HOST"] = os.getenv("PGHOST", "127.0.0.1")  # noqa: F405
DATABASES["default"]["PORT"] = os.getenv("PGPORT", "5433")  # noqa: F405
DATABASES["default"]["NAME"] = os.getenv("PGDATABASE", "pilotage_django")  # noqa: F405
DATABASES["default"]["USER"] = os.getenv("PGUSER", "postgres")  # noqa: F405
DATABASES["default"]["PASSWORD"] = os.getenv("PGPASSWORD", "password")  # noqa: F405
