import os

from config.settings.test import *  # noqa: F403


# Django settings
# ---------------
DEBUG = True

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False

SECURE_HSTS_INCLUDE_SUBDOMAINS = False

SECURE_HSTS_PRELOAD = False

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

AUTH_PASSWORD_VALIDATORS = []  # Avoid password strength validation in DEV.

INSTALLED_APPS.extend(  # noqa: F405
    [
        "debug_toolbar",
    ]
)

INTERNAL_IPS = ["127.0.0.1"]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405

# Don't use json formatter in dev
del LOGGING["handlers"]["console"]["formatter"]  # noqa: F405

# Project settings
# ----------------

METABASE_SECRET_KEY = os.getenv("METABASE_SECRET_KEY")
