from core.settings.orghierarchy import *  # noqa: F403

try:
    from rich.highlighter import ReprHighlighter
except ImportError:
    pass

else:
    LOGGING['handlers']['console'] = {  # noqa: F405
        'level': 'DEBUG',
        'formatter': 'dev',
        'class': 'rich.logging.RichHandler',
        'rich_tracebacks': True,
        'show_time': False,
        'show_path': False,
        'enable_link_path': False,
        'highlighter': ReprHighlighter(),
        'markup': True,
    }

# Place after `django.contrib.staticfiles'`
INSTALLED_APPS += ['debug_toolbar']  # noqa: F405
MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')  # noqa: F405
INTERNAL_IPS = ('127.0.0.1', '0.0.0.0:8000')
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False, 'TAG': 'body'}
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.history.HistoryPanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.alerts.AlertsPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
)
