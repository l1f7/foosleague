"""Development settings and globals."""


from os.path import join, normpath

from settings_base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION

SECRET_KEY = r"t4%w_uy@-hr!_e@pm9h4694&amp;t2*=r^mp4vw#dsvfh_+41$yfx+"

########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'foosleague',    # Or path to database file if using sqlite3.
        'USER': '',             # Not used with sqlite3.
        'PASSWORD': '',     # Not used with sqlite3.
        'HOST': '',   # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                 # Set to empty string for default. Not used with sqlite3.
    }
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
########## END CACHE CONFIGURATION


########## TOOLBAR CONFIGURATION
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INSTALLED_APPS += (
    'debug_toolbar',
)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ('127.0.0.1',)

########## END TOOLBAR CONFIGURATION

try:
    from local_dev import *
except ImportError:
    pass
