import copy

from django.conf import settings
from django.db.models.enums import TextChoices
from django.http import (
    JsonResponse,
)

from pilotage.itoutils import metabase
from pilotage.itoutils.departments import DEPARTMENTS


class DataSetName(TextChoices):
    DI_SERVICES = "di_services", "data·inclusion - Services"
    DI_STRUCTURES = "di_structures", "data·inclusion - Structures"


QUERIES = {
    DataSetName.DI_SERVICES: {
        "database": 2,
        "type": "query",
        "query": {
            "source-table": 2052,
            "fields": [
                ["field", 59639, {"base-type": "type/Text"}],  # ID
                ["field", 59644, {"base-type": "type/Text"}],  # Structure ID
                ["field", 59647, {"base-type": "type/Text"}],  # Source
                ["field", 59614, {"base-type": "type/Text"}],  # Nom
                ["field", 59643, {"base-type": "type/*"}],  # Thematiques
                ["field", 59627, {"base-type": "type/*"}],  # Frais
                ["field", 59636, {"base-type": "type/*"}],  # Profils
                ["field", 59649, {"base-type": "type/Text"}],  # Commune
                ["field", 59623, {"base-type": "type/Text"}],  # Code Postal
                ["field", 59654, {"base-type": "type/Text"}],  # Code Insee
                ["field", 59615, {"base-type": "type/Text"}],  # Adresse
                ["field", 59629, {"base-type": "type/Float"}],  # Longitude
                ["field", 59651, {"base-type": "type/Float"}],  # Latitude
                ["field", 59624, {"base-type": "type/*"}],  # Modes Accueil
            ],
            "filter": [
                "starts-with",
                ["field", 59654, {"base-type": "type/Text"}],
                "000",  # Default to no-matchs
                {"case-sensitive": False},
            ],
        },
    },
    DataSetName.DI_STRUCTURES: {
        "database": 2,
        "type": "query",
        "query": {
            "source-table": 2051,
            "fields": [
                ["field", 59591, {"base-type": "type/Text"}],  # ID
                ["field", 59600, {"base-type": "type/Text"}],  # Nom
                ["field", 59608, {"base-type": "type/Text"}],  # Commune
                ["field", 59606, {"base-type": "type/Text"}],  # Code Postal
                ["field", 59588, {"base-type": "type/Text"}],  # Code Insee
                ["field", 59605, {"base-type": "type/Text"}],  # Adresse
                ["field", 59594, {"base-type": "type/Float"}],  # Longitude
                ["field", 59599, {"base-type": "type/Float"}],  # Latitude
                ["field", 59590, {"base-type": "type/Text"}],  # Typologie
            ],
            "filter": [
                "starts-with",
                ["field", 59588, {"base-type": "type/Text"}],
                "000",  # Default to no-matchs
                {"case-sensitive": False},
            ],
        },
    },
}


def dataset(request, name):
    if name not in DataSetName:
        return JsonResponse({"error": "Dataset doesn't exists"}, status=404)

    # TODO: Use a query-builder like function to avoid a global and copying the query
    query = copy.deepcopy(QUERIES[DataSetName(name)])
    if department := request.GET.get("department"):
        if department not in DEPARTMENTS:
            return JsonResponse({"error": "Department doesn't exists"}, status=400)
        query["query"]["filter"][2] = department
    else:
        return JsonResponse({"error": "Department is a required query parameter"}, status=400)

    return JsonResponse(
        metabase.Client(settings.METABASE_BASE_URL).fetch_dataset_results(query),
        safe=False,  # Metabase return a list
    )
