from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE', default='django.db.backends.mysql'),
        'NAME': config('DB_NAME', default='test_db'),
        'USER': config('DB_USER', default='root'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default='127.0.0.1'),
        'PORT': config('DB_PORT', default='3306'),
        'TEST': {
            'NAME': 'test_db',  # évite que Django essaie de créer test_test_db
        }
    }
}
