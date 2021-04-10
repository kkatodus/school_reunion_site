from .settings_common import *
import os
import mimetypes
mimetypes.add_type("text/css", ".css", True)


DEBUG=True
MEDIA_ROOT=os.path.join(BASE_DIR,"media")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,"static"),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "dousoukai_event",
        'USER':os.environ.get("DB_USER"),
        'PASSWORD':os.environ.get("DB_PASSWORD"),
        "HOST":"",
        "PORT":"",
    }
}
