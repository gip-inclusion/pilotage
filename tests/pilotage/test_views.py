from django.urls import reverse
from freezegun import freeze_time

from pilotage.itoutils.tests import parse_response_to_soup


def test_home(snapshot, client):
    assert str(parse_response_to_soup(client.get(reverse("pilotage:home")), selector="#main")) == snapshot()


@freeze_time("2025-03-06")
def test_stats(snapshot, client):
    assert str(parse_response_to_soup(client.get(reverse("pilotage:statistiques")), selector="#main")) == snapshot()


def test_accessibilite(snapshot, client):
    assert str(parse_response_to_soup(client.get(reverse("pilotage:accessibilite")), selector="#main")) == snapshot()


def test_mentions_legales(snapshot, client):
    assert (
        str(parse_response_to_soup(client.get(reverse("pilotage:mentions_legales")), selector="#main")) == snapshot()
    )


def test_politique_de_confidentialite(snapshot, client):
    assert (
        str(parse_response_to_soup(client.get(reverse("pilotage:politique_de_confidentialite")), selector="#main"))
        == snapshot()
    )


def test_inscription_lettre_information(snapshot, client):
    assert (
        str(parse_response_to_soup(client.get(reverse("pilotage:inscription_lettre_information")), selector="#main"))
        == snapshot()
    )


def test_tableaux_de_bord_prives(snapshot, client):
    assert (
        str(parse_response_to_soup(client.get(reverse("pilotage:tableaux_de_bord_prives")), selector="#main"))
        == snapshot()
    )
