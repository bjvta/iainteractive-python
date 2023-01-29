from .base import *  # noqa

DEBUG = False
SECURE_SSL_HOST = True
UWSGI_CACHE_FALLBACK = True

INSTALLED_APPS += [
    "anymail",
    "raven.contrib.django.raven_compat"
]

ALLOWED_HOSTS = [f'{os.environ.get(("NAME_DOMAIN"))}', f'www.{os.environ.get(("NAME_DOMAIN"))}']

RAVEN_CONFIG = {
    "dsn": os.environ.get("SENTRY_DNS", "secret")
}


LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "sentry": {
            "level": "ERROR",
            "class": "raven.contrib.django.raven_compat.handlers.SentryHandler",
            "tags": {"custom-tag": "x"},
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "root": {"level": "WARNING", "handlers": ["sentry"]},
        "django.db.backends": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
        "raven": {"level": "DEBUG", "handlers": ["console"], "propagate": False},
        "sentry.errors": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}

EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
ANYMAIL = {
    "MAILGUN_API_KEY": os.environ.get("MAILGUN_API_KEY"),
    "MAILGUN_SENDER_DOMAIN": os.environ.get("MAILGUN_SENDER_DOMAIN"),
}