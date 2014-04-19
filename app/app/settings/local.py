from base import *


ALLOWED_HOSTS = ['*']

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'app.db',
    }
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../../srv/assets'),
)

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../../srv/static'))
STATIC_URL = 'http://local-static-david.ingledow.co.uk/'
