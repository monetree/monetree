import datetime

#soubhagyakumar666@gmail.com
# AWS_ACCESS_KEY_ID = 'AKIAJL4R5TFWJDSXDPZA'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'monetimes-django-static-bucket'
# S3DIRECT_REGION = 'ap-south-1'

#soubhagya.developer@gmail.com
AWS_ACCESS_KEY_ID = 'AKIAJFW75QDDDK5SCKPA'
AWS_SECRET_ACCESS_KEY = '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'

AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'monetimes.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'monetimes.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'django-static-file'
S3DIRECT_REGION = 'us-east-1'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}

AWS_QUERYSTRING_AUTH = True
