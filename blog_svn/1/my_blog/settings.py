"""
Django settings for my_blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import sys
reload(sys)
sys.setdefaultencoding('gbk')

if 'SERVER_SOFTWARE' in os.environ:
    import sae.const
    MYSQL_ENGINE = 'django.db.backends.mysql'
    MYSQL_DB = sae.const.MYSQL_DB
    MYSQL_USER = sae.const.MYSQL_USER
    MYSQL_PASS = sae.const.MYSQL_PASS
    MYSQL_HOST_M = sae.const.MYSQL_HOST
    MYSQL_HOST_S = sae.const.MYSQL_HOST_S
    MYSQL_PORT = sae.const.MYSQL_PORT
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG
    ALLOWED_HOSTS = ['zydmayday.sinaapp.com']
else:
    MYSQL_ENGINE = 'django.db.backends.sqlite3'
    MYSQL_DB = os.path.join(BASE_DIR, 'db.sqlite3')
    MYSQL_USER = ''
    MYSQL_PASS = ''
    MYSQL_HOST_M = ''
    MYSQL_HOST_S = ''
    MYSQL_PORT = ''
    
    # build mysql db in localhost
    # MYSQL_ENGINE = 'django.db.backends.mysql'
    # MYSQL_DB = 'blog'
    # MYSQL_USER = 'root'
    # MYSQL_PASS = '1234'
    # MYSQL_HOST_M = ''
    # MYSQL_HOST_S = ''
    # MYSQL_PORT = ''

    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    ALLOWED_HOSTS = []

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=$5e7%y9m@g-6$t6zlior4g7kta6%n+n-&iw_-bgzy!!motlq9'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False

# TEMPLATE_DEBUG = False

# ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'south',
    'article',
    'hitcount',
    'fantesysix',
    'spider',
    # 'bayes',
    'runfast',
    'history'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'my_blog.urls'

WSGI_APPLICATION = 'my_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': MYSQL_ENGINE,
        'NAME': MYSQL_DB,
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST': MYSQL_HOST_M,
        'PORT': MYSQL_PORT,  
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'
USE_TZ = True 

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static/'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'templates/'),
)

# hitcount configuration
HITCOUNT_KEEP_HIT_ACTIVE = { 'hours': 1 }
HITCOUNT_HITS_PER_IP_LIMIT = 0
HITCOUNT_EXCLUDE_USER_GROUP = ('zyd', )

# import logging
# logging.basicConfig(
#     level = logging.INFO,
#     format = '%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s',
#     filename = 'log.log',
#     )