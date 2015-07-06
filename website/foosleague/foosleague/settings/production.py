"""Production settings and globals."""


from os import environ

from settings_base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

# DEBUG = False
# TEMPLATE_DEBUG=DEBUG

def get_env_setting(setting):
	""" Get the environment setting or return exception """
	try:
		return environ[setting]
	except KeyError:
		error_msg = "Set the %s env variable" % setting
		raise ImproperlyConfigured(error_msg)


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'postmark.django_backend.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = "dev@liftinteractive.com"
DEFAULT_FROM_EMAIL = SERVER_EMAIL
########## END EMAIL CONFIGURATION


########## POSTMARK CONFIGURATION
POSTMARK_API_KEY = 'a876b1f2-2144-4e0a-9dbb-6fc2f801a3ff'
POSTMARK_SENDER = 'dev@liftinteractive.com'
POSTMARK_TEST_MODE = DEBUG
########## END POSTMARK CONFIGURATION


########## DATABASE CONFIGURATION
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
########## END CACHE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# SECRET_KEY = get_env_setting('SECRET_KEY')
########## END SECRET CONFIGURATION
SECRET_KEY = r"t4%w_uy@-hr!_e@pm9h4694&amp;t2*=r^mp4vw#dsvfh_+41$yfx+"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


ALLOWED_HOSTS = [
    '.foosleague.l1f7.com',
    '.leagueoffoos.com',
    'foosleague.com',
    'foosleague.tableofvictory.com',
]
########## RAVEN
# RAVEN_CONFIG = {
#     'dsn': '',
# }
########## END RAVEN

try:
    from local_production import *
except ImportError:
    pass
