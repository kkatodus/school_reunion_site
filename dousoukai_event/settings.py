from .settings_common import *

INSTALLED_APPS += ["storages",]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "dousoukai-event-database",
        'USER':os.environ.get("DB_USER"),
        'PASSWORD':os.environ.get("DB_PASSWORD"),
        "HOST":"dousoukai-event-database.cdve0djey2dy.ap-northeast-1.rds.amazonaws.com",
        "PORT":"5432",
    }
}

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = "dousoukai-event-bucket"
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_REGION_NAME = "ap-northeast-1"