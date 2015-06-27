"""
Django settings for codexapp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# MAILCHIMP API KEYS

MC_API_USERNAME = 'psiemens'
MC_API_KEY = '52e4e752068da129a885713f200740e8-us1'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_v%xhjs1bb#m2uzp8z#djioqx@ha@(^ljqybux*d3%4$04s63h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'codexapp.main',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'codexapp.urls'

WSGI_APPLICATION = 'codexapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'codex',
        'USER': 'codex',
        'PASSWORD': 'pKEXexaDRKEd3skh',
        'HOST': '192.241.201.61',
        'PORT': '3306'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Templates

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
    ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

BASE_STATIC_URL = 'http://localhost:8888/'

STATIC_URL = BASE_STATIC_URL + 'static/' # What do static URLs start with?
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # Where do static files live

