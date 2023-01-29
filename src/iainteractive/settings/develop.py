from .base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ["debug_toolbar"]  # noqa

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": (
        lambda request: not request.is_ajax()
        and request.path != "/"  # noqa: E731
    )
}


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp-server"
EMAIL_PORT = "1025"