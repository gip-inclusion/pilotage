import os

# Enable django-debug-toolbar with Docker.
import socket

from .base import *  # pylint: disable=wildcard-import,unused-wildcard-import # noqa: F403 F401


# Django settings
# ---------------
DEBUG = True

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

AUTH_PASSWORD_VALIDATORS = []  # Avoid password strength validation in DEV.
