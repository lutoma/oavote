# coding: utf-8
# Common parts between production and development settings

import os

SITE_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), os.path.pardir))
TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'de-de'
LANGUAGES = (
	('en', 'English'),
	('de', 'Deutsch'),
)

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
ROOT_URLCONF = 'oavote.urls'
WSGI_APPLICATION = 'oavote.wsgi.application'

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.humanize',
	'south',
	'django.contrib.admin',
	'django.contrib.admindocs',
	'vote',
	'votemail',
	'votefrontend',
	'votestatic'
)

MIDDLEWARE_CLASSES = (
	'django.middleware.gzip.GZipMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
	os.path.join(SITE_ROOT, 'templates'),
)

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATICFILES_DIRS = (
	os.path.join(SITE_ROOT, 'static'),
)

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse'
		}
	},
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
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

# Cache busting. Does nothing in development mode
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
