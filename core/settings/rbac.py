from core.settings.base import *  # noqa: F403

INSTALLED_APPS.insert(-1, 'rbac.apps.RbacConfig')  # noqa: F405

AUTHENTICATION_BACKENDS += [  # noqa: F405
    'rbac.backends.RbacUserBackend',
]

MIDDLEWARE += [  # noqa: F405
    'rbac.middleware.RbacSessionMiddleware',
]

AUTH_USER_MODEL = 'rbac.RbacUser'

# optional: Configure RBAC_DEFAULT_ROLES. This option accepts a tuple of role names which will be activated by default in RBAC sessions. If you omit this setting then all of the user's roles will be activated within a session.
# RBAC_DEFAULT_ROLES

# ROUTE_APP_LABELS += ('rbac',)

# print('ROUTE_APP_LABELS:', ROUTE_APP_LABELS)
