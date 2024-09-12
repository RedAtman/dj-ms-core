"""
refer: https://django-auditlog.readthedocs.io/
"""

from core.settings.celery import *  # noqa: F403

INSTALLED_APPS.insert(-1, 'auditlog')  # noqa: F405

MIDDLEWARE += [  # noqa: F405
    'auditlog.middleware.AuditlogMiddleware',
]

AUDITLOG_INCLUDE_ALL_MODELS=True
# AUDITLOG_EXCLUDE_TRACKING_FIELDS = (
#     "created",
#     "modified"
# )

# AUDITLOG_INCLUDE_TRACKING_MODELS = (
#     "<appname>.<model1>",
#     {
#         "model": "<appname>.<model2>",
#         "include_fields": ["field1", "field2"],
#         "exclude_fields": ["field3", "field4"],
#         "mapping_fields": {
#             "field1": "FIELD",
#         },
#         "mask_fields": ["field5", "field6"],
#         "m2m_fields": ["field7", "field8"],
#         "serialize_data": True,
#         "serialize_auditlog_fields_only": False,
#         "serialize_kwargs": {"fields": ["foo", "bar", "biz", "baz"]},
#     },
#     "<appname>.<model3>",
# )
