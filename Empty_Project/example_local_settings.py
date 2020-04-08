import os
from Empty_Project.settings import BASE_DIR

# SQlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# POSTGRESQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'db_name',
#         'HOST': 'db_host',
#         'PASSWORD': 'db_password',
#         'USER': 'dp_user',
#         'PORT': 5432
#     }
# }


# Email BACKEND
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
MAILER_EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_HOST = 'smtp server'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_HOST_USER = 'email address'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# from django.core.management.utils import get_random_secret_key
# new_key = get_random_secret_key()
SECRET_KEY = ''

