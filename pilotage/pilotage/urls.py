from django.urls import include, path
from . import views

app_name = "pilotage"
urlpatterns = [
    path("", views.home, name="home"),
    path("dashboards/", include("pilotage.dashboards.urls")),
    path("stats/", views.stats, name="statistiques"),
    path("accessibilite/", views.accessibilite, name="accessibilite"),
    path("mentions-legales/", views.mentions_legales, name="mentions_legales"),
    path(
        "politique-de-confidentialite/",
        views.politique_de_confidentialite,
        name="politique_de_confidentialite",
    ),
    path(
        "inscription-lettre-information/",
        views.inscription_lettre_information,
        name="inscription_lettre_information",
    ),
    path(
        "tableaux-de-bord-prives/",
        views.tableaux_de_bord_prives,
        name="tableaux_de_bord_prives",
    ),
]
