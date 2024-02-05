from django.contrib import admin
from django.urls import include, path
from pilotage.pilotage import urls as pilotage_urls
from pilotage.dashboards import urls as dashboards_urls

import os

urlpatterns = [
    path(os.environ["PATH_TO_ADMIN"], admin.site.urls),
    path("", include(pilotage_urls)),
    path("", include(dashboards_urls)),
]
