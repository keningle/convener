# Local Development Settings
from commune.settings.base import *
import commune.settings.secure as secure_settings
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'convener',
        'USER': 'convener',
        'PASSWORD': 'testpwd',
        'HOST': '',
        'PORT': '',
    }
}

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
MEDIA_ROOT = os.path.join(SITE_ROOT, '../../../media')
MEDIA_URL = 'http://localhost:8000/media/'
STATIC_ROOT = os.path.join(SITE_ROOT, '../../../static')
STATIC_URL = 'http://localhost:8000/static/'
STATICFILES_DIRS = ()
TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, '../../templates'),
)

SECRET_KEY = secure_settings.SECRET_KEY

# Locally only installed development apps, core apps are part of base.py
INSTALLED_APPS += ('debug_toolbar',)
INTERNAL_IPS = ("127.0.0.1",)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
