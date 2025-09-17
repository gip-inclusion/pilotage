from django.urls import path

from pilotage.surveys import views


app_name = "surveys"
urlpatterns = [
    path("<slug:name>", views.show, name="show"),
]
