import os
from os.path import abspath, join

# from django.utils.translation import ugettext_lazy as _

from ashe.utils import loadenv

gettext = lambda s: s

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

location = lambda path: abspath(join(BASE_DIR, path))
loadenv(location("../.env"))


SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "secret")
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "widget_tweaks",
    "iainteractive.apps.common",
    'rest_framework',
    'drf_yasg',
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

ROOT_URLCONF = "iainteractive.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "templates/")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

REST_FRAMEWORK = { 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema' }

WSGI_APPLICATION = "iainteractive.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": os.environ.get("DJANGO_DATABASE_HOST", "database"),
        "NAME": os.environ.get("DJANGO_DATABASE_NAME", None),
        "USER": os.environ.get("DJANGO_DATABASE_USER", None),
        "PASSWORD": os.environ.get("DJANGO_DATABASE_PASSWORD", "postgres"),
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

# DATE_INPUT_FORMATS = ("%d %b %Y",)
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = False
USE_TZ = True
SITE_ID = 1
LANGUAGES = [
    ("en", ("english")),
]

LOCALE_PATHS = [os.path.join(BASE_DIR, "../locale")]


X_FRAME_OPTIONS = "SAMEORIGIN"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "../frontend/dist"),
    os.path.join(PROJECT_DIR, "static/"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "../public/static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "../public/media")
MEDIA_URL = "/media/"
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

