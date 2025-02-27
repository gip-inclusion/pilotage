import pytest
from django.urls import reverse

from pilotage.api.views import DataSetName


@pytest.mark.parametrize("dataset_name", DataSetName)
def test_dataset(mocker, faker, client, dataset_name):
    expected_data = [faker.pydict(allowed_types=[str, int])]
    mocker.patch("itoutils.metabase.Client.fetch_dataset_results", return_value={"data": expected_data})

    assert client.get(reverse("api:dataset", kwargs={"name": dataset_name})).json() == expected_data
