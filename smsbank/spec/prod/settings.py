# -*- coding: utf-8 -*-
from smsbank.settings import *

WSGI_APPLICATION = 'smsbank.spec.prod.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'smsbank',
        'USER': 'root',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
