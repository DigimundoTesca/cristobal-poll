from poll.settings.dev import *

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('CRISTOBAL_POLL_DB_NAME'),
        'USER': os.getenv('CRISTOBAL_POLL_DB_USER'),
        'PASSWORD': os.getenv('CRISTOBAL_POLL_DB_PASSWORD'),
        'HOST': os.getenv('CRISTOBAL_POLL_DB_HOST'),
        'PORT': os.getenv('CRISTOBAL_POLL_DB_PORT'),
    }
}
