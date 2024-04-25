# test_settings.py

from .settings import *

# Use um banco de dados SQLite em memória para testes
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}