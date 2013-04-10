# coding: utf-8
# Development settings

# import intentionally not used here
execfile('oavote/settings-common.py')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	# This email address discards everything sent to it
	('Dev Null', 'devnull@ohai.su'),
)

MANAGERS = ADMINS

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': 'development.db',
		'USER': '',
		'PASSWORD': '',
		'HOST': '',
		'PORT': '',
	}
}

MEDIA_ROOT = '/tmp/oavote-asset/'
MEDIA_URL = '/asset/'
STATIC_ROOT = '/tmp/oavote-static/'
STATIC_URL = '/static/'
SECRET_KEY = ')%39c_8s*r)&amp;gmxa%nrpvc9-w_=azvyt)%27a^c%t*13ob1%=!'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
		'LOCATION': 'oavote'
	}
}
