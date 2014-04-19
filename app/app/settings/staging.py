from base import *

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

AWS_STORAGE_BUCKET_NAME = 'ingledow-staging'

STATIC_URL = 'http://ingledow-staging.s3.amazonaws.com/'
