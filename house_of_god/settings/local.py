from .base import *  # noqa
from .base import env

DEBUG = False


ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # noqa F405

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST', default='mailhog')
EMAIL_PORT = 1025

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']
