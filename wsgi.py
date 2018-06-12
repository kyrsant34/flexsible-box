"""
WSGI config for calculator project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import path
import os
import sys

from django.core.wsgi import get_wsgi_application


PROJECT_ROOT = path.Path(__file__).dirname()
sys.path.append(PROJECT_ROOT)
sys.path.append(PROJECT_ROOT / "apps")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()
