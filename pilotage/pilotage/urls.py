"""
URL configuration for pilotage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'pilotage'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
	path('dashboards/', include('dashboards.urls')),
    path('stats/', views.stats, name="statistiques"),
    path('accessibilite/', views.accessibilite, name="accessibilite"),
    path('mentions-legales/', views.mentions_legales, name="mentions_legales"),
    path('politique-de-confidentialite/', views.politique_de_confidentialite, name="politique_de_confidentialite"),
    path('inscription-lettre-information/', views.inscription_lettre_information, name="inscription_lettre_information"),
    path('tableaux-de-bord-prives/', views.tableaux_de_bord_prives, name="tableaux_de_bord_prives"),
]
