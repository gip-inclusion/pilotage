from config.settings.base import *  # noqa: F403


# Django settings
# ---------------

SECRET_KEY = "53cr37_k3y"

ALLOWED_HOSTS = []

SECURE_SSL_REDIRECT = False

DATABASES["default"]["HOST"] = os.getenv("PGHOST", "127.0.0.1")  # noqa: F405
DATABASES["default"]["PORT"] = os.getenv("PGPORT", "5432")  # noqa: F405
DATABASES["default"]["NAME"] = os.getenv("PGDATABASE", "pilotage")  # noqa: F405
DATABASES["default"]["USER"] = os.getenv("PGUSER", "postgres")  # noqa: F405
DATABASES["default"]["PASSWORD"] = os.getenv("PGPASSWORD", "password")  # noqa: F405

# Project settings
# ----------------

METABASE_SECRET_KEY = "m374b453_53cr37_k3y"
