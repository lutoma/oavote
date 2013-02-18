# coding: utf-8
# Production settings

# import intentionally not used here
execfile('aovote/settings-common.py')

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('Junge Piraten IT', 'it@junge-piraten.de'),
)

MANAGERS = ADMINS

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'aovote',
		'USER': 'aovote',
		'PASSWORD': '',
		'HOST': 'storage',
		'PORT': '',
	}
}

MEDIA_ROOT = '/tmp/aovote-asset/'
MEDIA_URL = '/asset/'
STATIC_ROOT = '/tmp/aovote-static/'
STATIC_URL = '/static/'

with file('/etc/aovote-secret') as key_file:
    SECRET_KEY = key_file.read()
