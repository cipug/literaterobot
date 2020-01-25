from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cipug',
        'USER': 'cipug',
        'PASSWORD': 'cipug',
        'HOST': 'localhost',
        'PORT': '',
    }
}


WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.contrib.postgres_search.backend',
    },
}