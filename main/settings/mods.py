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

# paypal stuff
PAYPAL_CLIENT_ID =  env('PAYPAL_CLIENT_ID')  #'AR5llBzLm0E7y9fGHaAoDHDg3zxq7-P-rp26RuoH8wQ7xPDOVtnL3KgPY1l3hgGzFXRRm_EXTyYnrkgS'
PAYPAL_CLIENT_SECRET = env('PAYPAL_CLIENT_SECRET') #'EJao2u8BaU6UZhmKhq14tEGlbEqAMrXKKDP8k4Dva4X1hnEtvZAcipTdCIa6nS3D9tEDtC02o7o2umkz'
PAYPAL_MODE = env('PAYPAL_MODE') #"sandbox" (or "live") 


