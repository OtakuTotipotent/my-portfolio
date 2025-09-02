# portfolio_project/settings/production.py
from decouple import config, Csv
from .base import *

# Debugging: Always False in production
DEBUG = config("DEBUG", default=False, cast=bool)

# Secret key: Load from environment variable
SECRET_KEY = config("SECRET_KEY")

# Allowed hosts: Comma-separated list from environment variable
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# Database configuration
# For SQLite (temporary for development, not recommended for production)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# For PostgreSQL (recommended for production)
# DATABASES = {
#     'default': dj_database_url.config(
#         default=config('DATABASE_URL')
#     )
# }

# Static files configuration for production
STATIC_ROOT = BASE_DIR / "staticfiles"  # Where collectstatic will put files
