import os
from os import environ
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = environ.get(
    'SECRET_KEY',
    '##%he5sc1%^9oqlf=dq8ae&k1kw(17q^)-=%f7u$rq9)_d06g_')

# allow debug to be set from env config
DEBUG = True if environ.get('DEBUG') is True else False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['.herokuapp.com', '.ingledow.co.uk', ]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gunicorn',
    'south',
    'blog',
    'markdown_deux',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'

DATABASES = {}
DATABASES['default'] = dj_database_url.config()

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../../srv/assets'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, '../templates/'),
)
LOGGING = {
    'version': 1,
}
