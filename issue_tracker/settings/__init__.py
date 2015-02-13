"""Settings for multiple configurations.

'prod.py' is the container for default settings which should be used by all
deployments of this application.

'local.py' is the developer specific settings.
"""

try:
    # The first line of local.py should be "from default import *", then it
    # can override those settings it sees fit.
    from local import *
except ImportError:
    from default import *
