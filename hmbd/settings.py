# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Django settings for hmbd project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from conf.dbconf import MYSQL_DB_MAIN, MYSQL_HOST_MAIN, MYSQL_PORT_MAIN, MYSQL_PWD_MAIN, MYSQL_USER_MAIN

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd0m-!yhakfswln02^x1igagew1!erjj3cyqs4u_qq#pg_v1#ca'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']
# Application definition

INSTALLED_APPS = (
    # django 默认,可以注释
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 自己的app目录
    'app',
)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.csrf.CsrfViewMiddleware'
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # mysql数据库
        'NAME': MYSQL_DB_MAIN,  # 数据库名
        'USER': MYSQL_USER_MAIN,  # 用户名
        'PASSWORD': MYSQL_PWD_MAIN,  # 密码
        'HOST': MYSQL_HOST_MAIN,  # 主机   默认：localhost
        'PORT': MYSQL_PORT_MAIN,  # 端口号 默认：3306
        'OPTIONS': {
            'autocommit': True,
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        "OPTIONS": {
            "CLIENT_CLASS": "redis_cache.client.DefaultClient",
        },
    },
}
ROOT_URLCONF = 'hmbd.urls'
WSGI_APPLICATION = 'hmbd.wsgi.application'

# 模板页目录配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
            ]
        }
    },
]

# TEMPLATE_DIRS = (
#     # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
#     # Always use forward slashes, even on Windows.
#     # Don't forget to use absolute paths, not relative paths.
#     BASE_DIR + "/template",
# )
# 设置语言
LANGUAGE_CODE = 'en'

# 设置支持的语言
LANGUAGES = (('zh-cn', u'中文'), ('en', u'English'))
'''LANGUAGES = (
    ('zh-cn', _('Chinese')),
    ('en', _('English')),
)'''
LANGUAGES_SUPPORTED = ('en', 'zh-cn',)
# 设置时区
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static') #
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
LOGIN_URL = 'login'

# 系统日志配置-----------------------------Begin-------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "simple": {
            "format": '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s'
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "all": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "when": "D",
            "interval": 1,
            "filename": os.path.join(BASE_DIR, "log/debug.log")
        }
    },
    "loggers": {
        "all": {
            "level": "DEBUG",
            "handlers": ["all"],
            "propagate": False
        },
        "console": {
            "level": "NOTSET",
            "handlers": ["console"],
            "propagate": False
        }
    },
    "root": {
        "level": "NOTSET",
        "handlers": ["console", "all"],
        "propagate": True
    }
}
# 系统日志配置-----------------------------End-------------------------------------
