import random

import pytest
from django.urls import reverse

from pilotage.api.views import DataSetName
from pilotage.itoutils import departments


@pytest.mark.parametrize("dataset_name", DataSetName)
def test_dataset(mocker, faker, client, dataset_name):
    expected_data = [faker.pydict(allowed_types=[str, int])]
    mocker.patch("pilotage.itoutils.metabase.Client.fetch_dataset_results", return_value=expected_data)

    response = client.get(
        reverse("api:dataset", kwargs={"name": dataset_name}),
        query_params={"department": random.choice(list(departments.DEPARTMENTS.keys()))},
    )
    assert response.json() == expected_data


def test_dataset_with_unknown_name(client, snapshot):
    response = client.get(reverse("api:dataset", kwargs={"name": "unknown"}))
    assert response.status_code == 404
    assert response.json() == snapshot()


@pytest.mark.parametrize("dataset_name", DataSetName)
def test_dataset_without_department(snapshot, client, dataset_name):
    response = client.get(reverse("api:dataset", kwargs={"name": dataset_name}))
    assert response.status_code == 400
    assert response.json() == snapshot()


@pytest.mark.parametrize("dataset_name", DataSetName)
def test_dataset_with_unknown_department(snapshot, client, dataset_name):
    response = client.get(reverse("api:dataset", kwargs={"name": dataset_name}), query_params={"department": "00"})
    assert response.status_code == 400
    assert response.json() == snapshot()
