import os, environ
from .main import INSTALLED_APPS, MIDDLEWARE, BASE_DIR

INSTALLED_APPS += [
    "environ",
    "main.hello",
    "djpaypal"
]

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ because of casting above
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")


# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# Parse database connection url strings
# like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises
    # ImproperlyConfigured exception if not found
    'default': env.db_url(
        'DATABASE_URL',
        default='sqlite:////tmp/my-tmp-sqlite.db'
    )
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# paypal stuff
PAYPAL_CLIENT_ID =  env('PAYPAL_CLIENT_ID')
PAYPAL_CLIENT_SECRET = env('PAYPAL_CLIENT_SECRET')
PAYPAL_MODE = env('PAYPAL_MODE') #"sandbox" (or "live") 
PAYPAL_WEBHOOK_ID = env('PAYPAL_WEBHOOK_ID')
