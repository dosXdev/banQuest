"""
Django settings for banquest project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+tt@hlm__$($i98e)^3%=o5j*21md+b&$%o(n)4(1lo+4koxbd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# host ip has to be added to this list
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'banquest',
    'api.apps.ApiConfig',
    'corsheaders', # cors header policy for react comm.
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

# CSRF cookie settings
CSRF_TRUSTED_ORIGINS = ['http://localhost:3000','http://127.0.0.1:3000']
CSRF_COOKIE_NAME = 'XSRF-TOKEN'
CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'

# required for CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Assuming UI is running on this origin
    "http://127.0.0.1:3000",
    # more origins to be added as needed
]

CORS_ALLOW_CREDENTIALS = True  # to include cookies in cross-origin requests

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]

CORS_ALLOW_HEADERS = [
    'Accept',
    'Accept-Language',
    'Content-Type',
    'Authorization',
    'X-CSRFToken',
]

ROOT_URLCONF = 'banquest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'banquest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    # local PostgreSQL setup
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # in future will come from config file
        'NAME': 'banQuest',  # in future will come from config file
        'USER': 'postgres', # in future will come from config file
        'PASSWORD': 'sneh@123',  # in future will come from config file
        'HOST': '172.28.128.1',  # ipv4 address of host server
        'PORT': '5432',  # in future will come from config file
    }
    # Dev RDS instance
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'banQuest',
    #     'USER': 'admin_user',
    #     'PASSWORD': '<pw-from-secrets-manager>',
    #     'HOST': 'banquest.cns2m40s6n98.ap-south-1.rds.amazonaws.com',
    #     'PORT': '5432',
    # }
}

# cmd to connect to Dev RDS via Ec2
# psql --host=banquest.cns2m40s6n98.ap-south-1.rds.amazonaws.com --port=5432 --username=admin_user --dbname=banQuest

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Disable rest default api view
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES':(
        'rest_framework.renderers.JSONRenderer',
                                )
}