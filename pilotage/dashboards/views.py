from django.shortcuts import render

from dashboards.models import Category, Dashboard


def tableaux_de_bord_publics(request):
    dashboards = Dashboard.objects.filter(active=True)
    categories = Category.objects.all()
    return render(
        request,
        "dashboards/tableaux_de_bord_publics.html",
        context={"dashboards": dashboards, "categories": categories},
    )


def tableau_de_bord_public(request, slug):
    dashboard = Dashboard.objects.get(slug=slug)
    return render(
        request,
        "dashboards/tableau_de_bord_public.html",
        context={"dashboard": dashboard, "slug": slug},
    )
