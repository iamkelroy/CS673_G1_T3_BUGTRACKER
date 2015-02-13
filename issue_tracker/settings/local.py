"""A local settings template.

Be careful changing this file as it will affect all development users.
"""

import fnmatch
# * imports should really never be used. Given this is passing settings around,
# this particular setup is getting a special pass.
from default import *


# local settings
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Set this to wherever you want to connect to. It is currently setup to
# run against sqlite.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/dev.db',
    }
}


if DEBUG:
    # set INTERNAL_IPS to entire local network
    class CheckLocalNetwork(list):
        def __contains__(self, key):
            for address in self:
                if fnmatch.fnmatch(key, address):
                    return True
            return False

    INTERNAL_IPS = CheckLocalNetwork(['127.0.0.1', '192.168.*.*'])

    # Additive installed apps.
    INSTALLED_APPS += (
    )

    # Additive middleware classes
    MIDDLEWARE_CLASSES += (
    )
