"""
Django settings for allwisp project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from django.conf.urls.static import static

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zl0p9j#6p&=e0f@ja%z2tn4+)uj_@#pru0yhwp2_*0*)#1n^t2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
	'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
	'django.contrib.humanize',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'django.contrib.sites',
	'cms',
	'menus',
	'treebeard',
	'sekizai',
	'djangocms_text_ckeditor',
	'djangocms_link',
	'djangocms_file',
	'djangocms_picture',
	'djangocms_video',
	'djangocms_googlemap',
	'djangocms_snippet',
	'djangocms_style',
	'filer',
	'easy_thumbnails',
	'mptt',
	'todo',
	'crispy_forms',
    'taggit',
	'notes',
    'apps.customer.apps.CustomerConfig' ,
    'apps.invoices.apps.InvoicesConfig',
    'apps.items.apps.ItemsConfig',
    'apps.reports.apps.ReportsConfig',
    'apps.expenses.apps.ExpensesConfig',
    'apps.attachment.apps.AttachmentConfig',
    'apps.azienda.apps.AziendaConfig',
    'commonviews.apps.CommonviewsConfig',
    'localflavor',
    'internationalflavor', 
    'phonenumber_field',
    'babel'
]

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

SITE_ID = 1

MIDDLEWARE = [
	'cms.middleware.utils.ApphookReloadMiddleware',
	'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'cms.middleware.user.CurrentUserMiddleware',
	'cms.middleware.page.CurrentPageMiddleware',
	'cms.middleware.toolbar.ToolbarMiddleware',
	'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'allwisp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
				'sekizai.context_processors.sekizai',
				'cms.context_processors.cms_settings',
				'django.template.context_processors.i18n',
				
            ],
        },
    },
]

CMS_TEMPLATES = [
	('home.html', 'Home page template'),
	('frontend_index.html', 'index template'),
]

WSGI_APPLICATION = 'allwisp.wsgi.application'

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR , 'db.sqlite3'),
    }
}


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

LANGUAGES = [
    ('en-us', 'English'),
    ('it-it', 'Italian'),
]

TIME_ZONE =  'Europe/Rome'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

X_FRAME_OPTIONS = 'SAMEORIGIN'

TODO_DEFAULT_LIST_SLUG = 'sitoweb'

EMAIL_USE_TLS = True
EMAIL_HOST = 'mail.arpanetitalia.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'service@arpanetitalia.com'
EMAIL_HOST_PASSWORD = 'arp$trSpd8889'
PHONENUMBER_DB_FORMAT = "INTERNATIONAL"