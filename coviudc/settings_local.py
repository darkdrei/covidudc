DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'coviudc',
        'USER': 'postgres',  # Database username
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

#CELERY_ALWAYS_EAGER = True


CELERY_RESULT_BACKEND = 'redis'
BROKER_URL = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['json', 'pickle']
#CELERY_TASK_SERIALIZER = 'pickle'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Bogota'


#ACCOUNT_EMAIL
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'darkdrei88@gmail.com'
EMAIL_HOST_PASSWORD = 'jzdjrxravolbweyd'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'CoroZina Test<zina.lat@nokia.com>'
