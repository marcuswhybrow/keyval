# Import the default settings for the project
from settings.default_settings import *

# If there are local settings, for example database credentials
# that are different for each installation, they override the
# defaults and are stored in local_settings.py
try:
    from settings.local_settings import *
except ImportError:
    pass