"""Default settings for the CS 673 Bugtracker project.

These are the settings used for production.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import os
import sys


DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Absolute paths for where the project and templates are stored.
ABSOLUTE_BASE_PATH = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
ABSOLUTE_TEMPLATES_PATH = '%s/templates' % ABSOLUTE_BASE_PATH

# Add root directory to the PYTHONPATH
if ABSOLUTE_BASE_PATH not in sys.path:
    sys.path.insert(0, ABSOLUTE_BASE_PATH)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = os.path.join(ABSOLUTE_BASE_PATH, 'static-collected')
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.join(ABSOLUTE_BASE_PATH, 'media')

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(ABSOLUTE_BASE_PATH, 'static-files')
)

# The URL that handles the media, static, etc.
STATIC_URL = '/static/'
MEDIA_URL = STATIC_URL + 'media/'


# Admins and managers.. Oh MY!
ADMINS = (
    ('Group1Team1', 'cs673s15t13@googlegroups.com'),
)

MANAGERS = ADMINS

# Unique key, generated from:
# http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = 'buggy*dd8zun6tda1&#rb#l@*201m%d(adroef523e!^^39j^&bzfx$cs673g1t3'


# List of finder classes that know how to find static files in
# various locations.
# https://docs.djangoproject.com/en/1.7/ref/settings/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# https://docs.djangoproject.com/en/1.7/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'issue_tracker.urls'
WSGI_APPLICATION = 'issue_tracker.wsgi.application'
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

TEMPLATE_DIRS = (
    # Don't forget to use absolute paths. No relative paths.
    ABSOLUTE_TEMPLATES_PATH,
)

# The apps are broken down to ensure better context around the purpose of the
# apps. As well, it gives an easy want to add to them when runnin in
# development mode.

# Placeholder for incorporating in admin tool apps.
ADMIN_TOOL_APPS = ()

# Apps that are provided by django.
CORE_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # django admin
    'django.contrib.admin',
    'django.contrib.admindocs',
)

# Placeholder for incorporating in external apps.
EXTERNAL_APPS = ()

# The local apps we have developed.
LOCAL_APPS = (
    'issue_tracker.app',
)

# The order is important!
# https://docs.djangoproject.com/en/1.7/ref/settings/#installed-apps
INSTALLED_APPS = ADMIN_TOOL_APPS + CORE_APPS + LOCAL_APPS + EXTERNAL_APPS

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'issue_tracker_app',
        'USER': 'issue_tracker_db_user',
        'PASSWORD': 'db_pw',  # TODO(jdarrieu): read db pw from local file.
        'HOST': '127.0.0.1',
        'PORT': '',  # Empty string == default port.
        }
}

# Allowed hosts
# https://docs.djangoproject.com/en/1.7/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ()

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

# Local time zone for installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# Windows users: Environment must be set to your local system's time zone.
# system time zone.
TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True
