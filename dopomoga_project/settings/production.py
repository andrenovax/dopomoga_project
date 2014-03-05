# Quick-start development settings - unsuitable for production https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
from .basic import *
import dj_database_url


SECRET_KEY = 'ft%f#%f_*r7d-%*a#28&tijrpyt$vc!b=x)@t#7g4i!@tf)(-!'
TEMPLATE_DEBUG = True


#===============CHANGE===============
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['.dopomoga.herokuapp.com']
# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()


#===============ADD==================
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)


ADMINS = (('Andrey', 'andrenovax@gmail.com'), )
MANAGERS = ADMINS
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
