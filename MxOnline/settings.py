# coding: utf-8
"""
Django settings for MxOnline project.

Generated by 'django-admin startproject' using Django 1.9.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DIR = os.path.join(BASE_DIR, 'apps')
EXTRA_APPS = os.path.join(BASE_DIR, 'extra_apps')
sys.path.insert(0, APP_DIR)
sys.path.insert(0, EXTRA_APPS)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_itvl5og!sc%0wt$bo!**o*hyu7@h8f&xn*8ty-qt!_i34_2px'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'courses',
    'organization',
    'operation',
    'xadmin',
    'crispy_forms',
    'captcha',
    'pure_pagination',
    'DjangoUeditor'
]

# 配置自定义的user表
# 配置好后再执行makemigrations 和 migrate
AUTH_USER_MODEL = 'users.UserProfile'

# 自定义登录函数配置
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)

# session过期时间配置
SESSION_COOKIE_AGE = 2*7*24*60*60

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MxOnline.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.media'   # media处理类, 注册MEDIA_URL
            ],
        },
    },
]

WSGI_APPLICATION = 'MxOnline.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mxonline',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'

# 中文
LANGUAGE_CODE = 'zh-hans'

# 时区：上海
TIME_ZONE = 'Asia/shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True

# 本地时间
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
"""
前端的静态文件路径两种配置方法：
1 绝对路径配置：/mystatic/css/test.css
2 相对路径配置："{% static 'css/test.css' %}"
"""
# 调用时的路径
STATIC_URL = '/static/'
# 实际具体的路径
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# 自己配置静态文件代理地址
# STATIC_ROOT = os.path.join(BASE_DIR, "static")


# 新浪邮件配置
# EMAIL_HOST = "smtp.sina.com"
# EMAIL_PORT = 25
# EMAIL_HOST_USER = "projectsedu@sina.com"
# EMAIL_HOST_PASSWORD = "admin123"
# EMAIL_USE_TLS= False
# EMAIL_FROM = "projectsedu@sina.com"

# QQ邮箱配置
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = '414820128@qq.com'  # 你的 QQ 账号
EMAIL_HOST_PASSWORD = "hwnhaoepeveycaee"  # '刚刚复制的授权码（不是你的 QQ 密码！！！）'开启服务：POP3/SMTP服务
EMAIL_USE_TLS = True  # 这里必须是 True，否则发送不成功
EMAIL_FROM = '414820128@qq.com'  # 你的 QQ 账号

# django-pure-pagination分页插件的配置
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 5,
    'MARGIN_PAGES_DISPLAYED': 2,

    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}
