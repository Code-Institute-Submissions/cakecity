"""
Django settings for cakecity project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DEVELOPMENT' in os.environ
# if DEBUG:
#     SITE_URL = 'http://127.0.0.1:8000/'

ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS = ['mat-cakecity.herokuapp.com', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'allauth',
    #'allauth.account',
    #'allauth.socialaccount',
    'web',
    'products',
    'cart',
    'checkout',
    'accounts',
    #Others
    'crispy_forms',
    'storages',
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cakecity.urls'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.contexts.cart_contents',
            ],
            'builtins':[
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]
        },
    },
]

WSGI_APPLICATION = 'cakecity.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': dj_database_url.parse('postgres://blxgjqeebvgjzk:84d0a744915c9c825b3a8f61a2c516f2d74f25290d8c69652f0109287c1ba324@ec2-18-203-62-227.eu-west-1.compute.amazonaws.com:5432/d57vufq2gk58ah')
# }

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse('postgres://blxgjqeebvgjzk:84d0a744915c9c825b3a8f61a2c516f2d74f25290d8c69652f0109287c1ba324@ec2-18-203-62-227.eu-west-1.compute.amazonaws.com:5432/d57vufq2gk58ah')
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'cakecity',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         'USER': 'root',
#         'PASSWORD': '',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#python manage.py makemigrations
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = (os.path.join(BASE_DIR, 'static'),)
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
# set session timeout
#SESSION_COOKIE_AGE = 120

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Stripe key SetUP
STRIPE_PUBLIC_KEY = 'pk_test_IsjjZmU79vK4VvuALK5XgACe'
STRIPE_SECRET_KEY = 'sk_test_mlH3zbcV2X2jdNkpdDujYe8a'
STRIPE_CURRENCY = 'eur'

# aws SetUP
if 'USE_AWS' in os.environ:
    # Bucket config
    AWS_STORAGE_BUCKET_NAME = 'cakecity-bucket'
    AWS_S3_REGION_NAME = 'EU (Ireland) eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
