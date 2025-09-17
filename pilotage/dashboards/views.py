from django.shortcuts import get_object_or_404, render

from pilotage.dashboards.models import Dashboard


def tableaux_de_bord_publics(request):
    dashboards = (
        Dashboard.objects.filter(active=True)
        .select_related("category")
        .order_by("category__display_order", "-category__pk", "-pk")
    )
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
        context={
            "dashboard": dashboard,
            "slug": slug,
            # Parameters for "partials/footer-scripts.html"
            "hasIframeResizer": not dashboard.embed_url,
            "hasIframeResizerFromOther": dashboard.embed_url,
            "hasTallyEmbed": dashboard.tally_embed_id,
            "hasTallyPopup": dashboard.tally_popup_id,
        },
    )
