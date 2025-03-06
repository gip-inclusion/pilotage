from django.shortcuts import get_object_or_404, render

from pilotage.dashboards.models import Dashboard


def tableaux_de_bord_publics(request):
    dashboards = Dashboard.objects.filter(active=True).select_related("category").order_by("-category__pk", "-pk")
    return render(
        request,
        "dashboards/tableaux_de_bord_publics.html",
        context={"dashboards": dashboards},
    )


def tableau_de_bord_public(request, slug):
    dashboard = get_object_or_404(Dashboard, slug=slug)
    return render(
        request,
        "dashboards/tableau_de_bord_public.html",
        context={"dashboard": dashboard, "slug": slug, "show_webinar_banner": False},
    )
