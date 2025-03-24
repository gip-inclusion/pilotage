from django.urls import path

from pilotage.api import views


app_name = "api"
urlpatterns = [
    path("dataset/<slug:name>", views.dataset, name="dataset"),
]
