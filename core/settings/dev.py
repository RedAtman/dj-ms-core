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
