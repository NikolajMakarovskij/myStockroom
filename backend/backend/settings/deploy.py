"""
Django settings for deploy.

"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = list(os.environ.get('DJANGO_ALLOWED_HOSTS').split(' '))

INSTALLED_APPS = [
    'rest_framework',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'workplace.apps.WorkplaceConfig',
    'employee.apps.EmployeeConfig',
    'software.apps.SoftwareConfig',
    'consumables.apps.ConsumablesConfig',
    'device.apps.DeviceConfig',
    'signature.apps.SignatureConfig',
    'counterparty.apps.CounterpartyConfig',
    'stockroom.apps.StockroomConfig',
    'decommission.apps.DecommissionConfig',
    'accounting.apps.AccountingConfig',
    'django.contrib.postgres',
    'django_bootstrap5',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_select2',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'stockroom.context_processors.stock',

            ],
        },
    },
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", ),
        "NAME": os.environ.get("SQL_DATABASE"),
        "USER": os.environ.get("SQL_USER"),
        "PASSWORD": os.environ.get("SQL_PASSWORD"),
        "HOST": os.environ.get("SQL_HOST"),
        "PORT": os.environ.get("SQL_PORT"),
        'CONN_MAX_AGE': 60 * 10,
    }
}

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

# start region settings

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Yekaterinburg'

USE_I18N = True

USE_TZ = True

DATE_FORMAT = 'd.m.Y'

# end region settings
# start file settings

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\', '/')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = 'media/'

MAX_UPLOAD_SIZE = "104857600"

# end file settings
# start caches


CACHES = {
    'default': {
        # 'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "db": "16",
    },
    'select2': {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://redis:6379/2",
        "db": "16",
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
SELECT2_CACHE_BACKEND = "select2"
# end caches

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/home/'

ROOT_URLCONF = 'backend.urls'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000000

CSRF_TRUSTED_ORIGINS = ['http://0.0.0.0']

STOCK_SESSION_ID = 'stock'
DECOM_SESSION_ID = 'decom'


# REST

def render_calasses():
    return [
        'rest_framework.renderers.JSONRenderer',
    ]


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': render_calasses(),
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DATE_INPUT_FORMATS': [
        '%d.%m.%Y',  # '25.10.2021'
        '%d.%m.%y',  # '25.10.21'
    ],
}
