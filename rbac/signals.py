import logging

logger = logging.getLogger(__name__)


def init(signal, sender, app_config, **kwargs):

    logger.info((signal, sender, app_config, kwargs))
    from rbac.init import Init
    Init().run()
