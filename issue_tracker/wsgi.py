"""What You What You Get (WSGI) application for bugtracker app.

This module contains the WSGI application provided by Django. It interacts
with Django's ``runserver`` and ``runfcgi`` commands discover this application
via the ``WSGI_APPLICATION`` setting.
"""
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'issue_tracker.settings')  # noqa

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
