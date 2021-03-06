"""
WSGI config for dousoukai_event project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

load_dotenv(varbose=True)

if os.environ.get('IS_DEV_ENV') == '1':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dousoukai_event.settings_dev')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dousoukai_event.settings')

application = get_wsgi_application()
