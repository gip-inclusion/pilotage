from django.shortcuts import render

from dashboards.models import Dashboard

def tableaux_de_bord_publics(request):
    dashboards = Dashboard.objects.all()
    return render(request, 'dashboards/tableaux_de_bord_publics.html', context={'dashboards': dashboards})

def tableau_de_bord_public(request):
    return render(request, 'dashboards/tableau_de_bord_public.html')
