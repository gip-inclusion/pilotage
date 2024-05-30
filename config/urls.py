from django.contrib import admin
from django.urls import include, path

from pilotage.dashboards import urls as dashboards_urls
from pilotage.pilotage import urls as pilotage_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(pilotage_urls)),
    path("", include(dashboards_urls)),
]
