from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.urls import reverse

BASE_DIR = Path(__file__).resolve().parent.parent.parent
APPS_DIRS = BASE_DIR/'apps'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# Application definition

BUILT_IN_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [
    'debug_toolbar',
    'phonenumber_field',
    'django_q'
]
USER_DEFINED_APPS = [
    'apps.blogs',
    'apps.commons',
    'apps.openings',
    'apps.products',
    'apps.team',
    'apps.services',
    #'apps.core',
]

INSTALLED_APPS = BUILT_IN_APPS + THIRD_PARTY_APPS + USER_DEFINED_APPS

BUILT_IN_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

USER_DEFINED_MIDDLEWARE = []
THIRD_PARTY_MIDDLEWARE = []

MIDDLEWARE = BUILT_IN_MIDDLEWARE + USER_DEFINED_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE

ROOT_URLCONF = 'Project2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'] ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.core.context_processors.user_defined_context.time_now',
            ],
        },
    },
]

WSGI_APPLICATION = 'Project2.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR.parent /'assets'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

Q_CLUSTER = {
    'name': 'project2',
    #'workers': 8,
    'recycle': 500,
    'retry':80,
    'timeout': 60,
    'compress': True,
    'save_limit': 250,
    'queue_limit': 500,
    'cpu_affinity': 1,
    'label': 'Django Q',
    'redis': {
        'host': 'localhost',
        'port': 6379,
        'db': 0,
        'password': None,
        'socket_timeout': None,
        'charset': 'utf-8',
        'errors': 'strict',
        'unix_socket_path': None
         }
}



LOGGING = {
    'version': 1,
    'loggers': {
        'custom_logger1':{
            'level':'INFO',
            'handlers':['custom_handler']
            },
        #'custom_logger2':{}

    },
    'handlers': {
        'custom_handler': {
            'level': 'INFO',
            'class':'logging.FileHandler',
            'filename': BASE_DIR/'logs/custom_handler.log'
        },
    }
}