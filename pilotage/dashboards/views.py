from django.shortcuts import render
from django.db.models import Prefetch

from pilotage.dashboards.models import Category, Dashboard

def tableaux_de_bord_publics(request):
    categories = Category.objects.all().prefetch_related(
        Prefetch(
            "dashboard_set",
            to_attr="dashboards",
            queryset=Dashboard.objects.filter(active=True),
        ),
    )
    return render(
        request,
        "dashboards/tableaux_de_bord_publics.html",
        context={"categories": categories},
    )


def tableau_de_bord_public(request, slug):
    dashboard = Dashboard.objects.get(slug=slug)

    return render(
        request,
        "dashboards/tableau_de_bord_public.html",
        context={"dashboard": dashboard, "slug": slug},
    )
