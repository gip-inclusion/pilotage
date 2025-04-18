from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from pilotage.api import urls as api_urls
from pilotage.dashboards import urls as dashboards_urls
from pilotage.pilotage import urls as pilotage_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_urls)),
    path("", include(pilotage_urls)),
    path("", include(dashboards_urls)),
]

if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
