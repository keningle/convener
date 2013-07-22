# Local Development Settings
from commune.settings.base import *
import commune.settings.secure as secure_settings
import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': secure_settings.DB_NAME,                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': secure_settings.DB_USER,
        'PASSWORD': secure_settings.DB_PWD,
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
MEDIA_ROOT = os.path.join(SITE_ROOT, '../../media')
MEDIA_URL = 'http://localhost:8000/media/'
STATIC_ROOT = os.path.join(SITE_ROOT, '../../static')
STATIC_URL = 'http://localhost:8000/static/'
STATICFILES_DIRS = ()
TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, '../templates'),
)

ALLOWED_HOSTS = []
SECRET_KEY = secure_settings.SECRET_KEY
