from .base import *

SECRET_KEY = 'django-insecure-^^^_n!ogkg8k_$c$q1)*=&=255%bs^n86s@uem2r(qiab+^#=3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


if DEBUG:
    INTERNAL_IP = [
        '127.0.0.1',
    ]
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]
    
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = []




# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = 'a8d7c422636633'
EMAIL_HOST_PASSWORD = '64cb9f1798e6c5'
EMAIL_PORT = '2525'

CACHES = {
    "default": {
        "BACKEND": "redis_cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "example"
    }
}