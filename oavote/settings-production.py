# coding: utf-8
# Production settings

# import intentionally not used here
execfile('oavote/settings-common.py')

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('Junge Piraten IT', 'it@junge-piraten.de'),
)

MANAGERS = ADMINS

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'oavote',
		'USER': 'oavote',
		'PASSWORD': '',
		'HOST': 'storage',
		'PORT': '',
	}
}

MEDIA_ROOT = '/tmp/oavote-asset/'
MEDIA_URL = '/asset/'
STATIC_ROOT = '/tmp/oavote-static/'
STATIC_URL = '/static/'

with file('/etc/oavote-secret') as key_file:
    SECRET_KEY = key_file.read()

ALLOWED_HOSTS = ['.junge-piraten.de', '127.0.0.1', '::1']

CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION': 'storage:11211',
	}
}

KEY_PREFIX = 'oavote'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mx'
DEFAULT_FROM_EMAIL = 'oa@junge-piraten.de'
EMAIL_SUBJECT_PREFIX = '[Junge Piraten] '

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
