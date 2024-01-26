from django.contrib import admin
from django.urls import path
from dashboards import views

app_name = 'dashboards'
urlpatterns = [
    path('tableaux-de-bord/', views.tableaux_de_bord_publics, name="tableaux_de_bord_publics"),
    path('tableau-de-bord/', views.tableau_de_bord_public, name="tableau_de_bord_public"),
]
