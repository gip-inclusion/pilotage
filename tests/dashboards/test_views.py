from django.core import management
from django.urls import reverse
from freezegun import freeze_time

from pilotage.itoutils.tests import parse_response_to_soup
from tests.dashboards.factories import DashboardFactory


def test_tableaux_de_bord_publics_without_dashboards(snapshot, client):
    assert (
        str(parse_response_to_soup(client.get(reverse("dashboards:tableaux_de_bord_publics")), selector="#main"))
        == snapshot()
    )


def test_tableaux_de_bord_publics_with_fixture_dashboards(snapshot, client):
    management.call_command(
        "loaddata",
        "pilotage/fixtures/dashboard.json",
    )
    assert (
        str(parse_response_to_soup(client.get(reverse("dashboards:tableaux_de_bord_publics")), selector="#main"))
        == snapshot()
    )


@freeze_time("2025-03-06")
def test_tableau_de_bord_public(snapshot, client):
    dashboard = DashboardFactory(
        for_snapshot=True,
    )

    assert (
        str(
            parse_response_to_soup(
                client.get(reverse("dashboards:tableau_de_bord_public", kwargs={"slug": dashboard.slug})),
                selector="#main",
            )
        )
        == snapshot()
    )
