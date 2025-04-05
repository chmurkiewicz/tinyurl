from pathlib import Path

import os

oeg = os.environ.get

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = oeg("TINYURL_DJANGO_SECRET_KEY", "change-on-production")

DEBUG = oeg("TINYURL_DJANGO_SECRET_KEY", "true").lower() == "true"

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "tinyurl",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "tinyurl.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "tinyurl.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": oeg("TINYURL_DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": oeg("TINYURL_DB_NAME", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": oeg("TINYURL_DB_USER", ""),
        "PASSWORD": oeg("TINYURL_DB_PASSWORD", ""),
        "HOST": oeg("TINYURL_DB_HOST", ""),
        "PORT": oeg("TINYURL_DB_PORT", ""),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = oeg("TINYURL_STATIC_URL", "static/")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Przedrostek używany do generowania skróconego url - powinien być taki sam jak host, na którym będzie stała aplikacja.
# 'http://' nie jest wymagane.
APPLICATION_HOST = oeg("TINYURL_APPLICATION_HOST", "http://localhost:8000")
# Jak długie mogą być urle przesyłane przez użytkowników do skrócenia.
MAX_URL_LENGTH = int(oeg("TINYURL_MAX_URL_LENGTH", "5000"))
