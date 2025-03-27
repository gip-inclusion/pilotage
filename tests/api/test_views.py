import pytest
from django.urls import reverse

from pilotage.api.views import DataSetName


@pytest.mark.parametrize("dataset_name", DataSetName)
def test_dataset(mocker, faker, client, dataset_name):
    expected_data = [faker.pydict(allowed_types=[str, int])]
    mocker.patch("pilotage.itoutils.metabase.Client.fetch_dataset_results", return_value=expected_data)

    response = client.get(
        reverse("api:dataset", kwargs={"name": dataset_name}), query_params={"department": faker.numerify("###")}
    )
    assert response.json() == expected_data


def test_dataset_with_unknown_name(client):
    assert client.get(reverse("api:dataset", kwargs={"name": "unknown"})).status_code == 404


@pytest.mark.parametrize("dataset_name", DataSetName)
def test_dataset_without_department(client, dataset_name):
    assert client.get(reverse("api:dataset", kwargs={"name": dataset_name})).status_code == 400
