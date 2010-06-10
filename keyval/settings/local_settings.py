import os
PATH = os.path.abspath(os.path.dirname(__file__))
from default_settings import *

# Specify a database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PATH, 'dev.db'),   # Or path to database file if using sqlite3.
    }
}

# Specifiy a secert key for Django
# I recommend a password from https://www.grc.com/passwords.htm (Steve Gibson is the man!)
SECRET_KEY = 'sWnsajmcyJGSoqkJAJi5y3cvLWH1CEyuTvBTQpB76o5IFh4ddptzvOQ9XEX6Zq2'

# Django Debug Toolbar
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INTERNAL_IPS = ('127.0.0.1',)
INSTALLED_APPS += ('debug_toolbar',)
DEBUG_TOOLBAR_CONFIG = { 'INTERCEPT_REDIRECTS': False }