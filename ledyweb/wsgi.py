"""
WSGI config for ledyweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import pathlib

from Home.views import FV
from ledyweb import wsgi_logger
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

os.environ['MPLCONFIGDIR'] = '/tmp/'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ledyweb.settings')


credential_path = str(pathlib.Path(__file__).parent.absolute())
credential_path= credential_path.split("ledypi")[0] + "ledypi/src/firebase/credential.json"

options=dict(
    credential_path=credential_path,
    databaseURL="https://ledypie.firebaseio.com/",
    debug=True)

FV.init_firebase(options)

if settings.DEBUG:
    wsgi_logger.info("Started debug")
    application = StaticFilesHandler(get_wsgi_application())
else:
    wsgi_logger.info("Started normal mode")

    application = get_wsgi_application()
