"""ms_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import logging
from importlib import import_module

from django.apps import apps
from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import URLResolver, include, path
from django.utils.text import slugify

logger = logging.getLogger(__name__)

URL_PREFIX = settings.APP_LABEL + '/' if settings.APP_LABEL else ''


urlpatterns = [
    path(URL_PREFIX + 'admin/', admin.site.urls),
    path('api/auth/', include('authentication.api.urls'), name='authentication'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


def get_redirect_url():
    if URL_PREFIX:
        return redirect(f'{URL_PREFIX}')
    return redirect(URL_PREFIX + 'admin/')


urlpatterns += [
    path('', lambda req: get_redirect_url()),
]

urlpatterns += [
    path('api/' + URL_PREFIX, include('app.api.urls'), name='api'),
    path(URL_PREFIX, include('app.urls')),
]


for app_config in apps.get_app_configs():
    try:
        mod = import_module("%s.%s" % (app_config.name, 'urls'))
        # logger.debug(('mod', app_config.name))
        # possibly cleanup the after the imported module?
        # might fuss up the `include(...)` or leave a polluted namespace
    except ImportError:
        # logger.error(('import error', app_config.name))
        # cleanup after module import if fails, maybe you can let the `include(...)` report failures
        pass
    else:
        url: URLResolver = path(r'%s/' % slugify(app_config.label), include('%s.urls' % app_config.name))
        # logger.debug((app_config.label, 'url', url))
        urlpatterns.append(url)
