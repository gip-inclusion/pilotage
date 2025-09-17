from django.urls import path

from pilotage.surveys import views


app_name = "surveys"
urlpatterns = [
    path("<slug:survey_name>/", views.start, name="start"),
    path("<slug:survey_name>/<uuid:answer_uid>/<str:step>", views.tunnel, name="tunnel"),
]
