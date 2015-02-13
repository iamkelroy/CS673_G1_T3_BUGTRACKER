"""A local settings template."""

import fnmatch
# * imports should really never be used. Given this is passing settings around,
# this particular setup is getting a special pass.
from default import *


def _CheckLocalNetwork(addresses):
    """Check whether the current IP matches the addresses provided.

    Args:
       addresses: A list of IP addresses which can be exanded via unix fnmatch.
    Returns:
       Boolean as to whether the current IP matches the provided IPs in the
       list.
    """
    for address in self:
        if fnmatch.fnmatch(key, address):
            return True
    return False

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
    INTERNAL_IPS = _CheckLocalNetwork(['127.0.0.1', '192.168.*.*'])

    # Additive installed apps for debugging.
    INSTALLED_APPS += (
    )

    # Additive middleware classes for debugging.
    MIDDLEWARE_CLASSES += (
    )
