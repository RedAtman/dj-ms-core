from core.settings.auditlog import *  # noqa: F403

INSTALLED_APPS.insert(-1, 'guardian')  # noqa: F405

AUTHENTICATION_BACKENDS += [  # noqa: F405
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend'
]
