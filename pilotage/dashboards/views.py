from django.http import HttpResponse
from django.shortcuts import render

from dashboards.models import Dashboard


def home(request):
    return render(request, 'pilotage/home.html')

def stats(request):
    return render(request, 'pilotage/statistiques.html')

def accessibilite(request):
    return render(request, 'pilotage/accessibilite.html')

def politique_de_confidentialite(request):
    return render(request, 'pilotage/politique_de_confidentialite.html')

def inscription_lettre_information(request):
    return render(request, 'pilotage/inscription_lettre_information.html')

def mentions_legales(request):
    return render(request, 'pilotage/mentions_legales.html')

def tableaux_de_bord_prives(request):
    return render(request, 'pilotage/tableaux_de_bord_prives.html')

def tableaux_de_bord_publics(request):
    dashboards = Dashboard.objects.all()
    return render(request, 'dashboards/tableaux_de_bord_publics.html', context={'dashboards': dashboards})
