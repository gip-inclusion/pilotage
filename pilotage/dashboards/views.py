from django.shortcuts import render

from pilotage.dashboards.models import Dashboard


def tableaux_de_bord_publics(request):
    dashboards = (
        Dashboard.objects.filter(active=True)
        .select_related("category")
        .order_by("-category__pk", "-pk")
    )
    return render(
        request,
        "dashboards/tableaux_de_bord_publics.html",
        context={"dashboards": dashboards},
    )


def tableau_de_bord_public(request, slug):
    dashboard = Dashboard.objects.get(slug=slug)

    return render(
        request,
        "dashboards/tableau_de_bord_public.html",
        context={"dashboard": dashboard, "slug": slug, "show_webinar_banner": False},
    )
