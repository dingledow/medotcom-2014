from base import *

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

AWS_STORAGE_BUCKET_NAME = 'ingledow-staging'

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../../srv/assets'),
)

STATIC_ROOT = 'http://ingledow-staging.s3.amazonaws.com/'
STATIC_URL = 'http://ingledow-staging.s3.amazonaws.com/'

MEDIA_ROOT = 'http://ingledow-media.s3.amazonaws.com/'
MEDIA_URL = 'http://ingledow-media.s3.amazonaws.com/'
