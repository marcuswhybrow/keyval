# Specify a database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                     # Or path to database file if using sqlite3.
        'USER': '',                     # Not used with sqlite3.
        'PASSWORD': '',                 # Not used with sqlite3.
        'HOST': '',                     # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                     # Set to empty string for default. Not used with sqlite3.
    }
}

# Specifiy a secert key for Django
# I recommend a password from https://www.grc.com/passwords.htm (Steve Gibson is the man!)
SECRET_KEY = ''

# Django Debug Toolbar
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INTERNAL_IPS = ('127.0.0.1',)
INSTALLED_APPS += ('debug_toolbar',)
DEBUG_TOOLBAR_CONFIG = { 'INTERCEPT_REDIRECTS': False }