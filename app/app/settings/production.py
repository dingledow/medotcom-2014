from base import *

DEBUG = True

TEMPLATE_DEBUG = True

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

AWS_STORAGE_BUCKET_NAME = 'ingledow-production'

STATICFILES_STORAGE = 'app.settings.s3utils.StaticRootS3BotoStorage'
DEFAULT_FILE_STORAGE = 'app.settings.s3utils.MediaRootS3BotoStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../../srv/assets'),
)

STATIC_ROOT = 'http://ingledow-production.s3.amazonaws.com/static/'
STATIC_URL = 'http://ingledow-production.s3.amazonaws.com/static/'

MEDIA_ROOT = 'http://ingledow-production.s3.amazonaws.com/media/'
MEDIA_URL = 'http://ingledow-production.s3.amazonaws.com/media/'
