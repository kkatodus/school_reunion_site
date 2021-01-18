from .settings_common import *
import os

MEDIA_ROOT=os.path.join(BASE_DIR,"media")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,"static"),
)
