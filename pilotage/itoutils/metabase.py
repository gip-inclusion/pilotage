import copy
import json
from urllib.parse import urljoin

import httpx
from django.conf import settings


# Metabase API client
# See: https://www.metabase.com/docs/latest/api/
class Client:
    def __init__(self, base_url):
        self._client = httpx.Client(
            base_url=urljoin(base_url, "/api"),
            headers={
                "X-API-KEY": settings.METABASE_API_KEY,
            },
            timeout=httpx.Timeout(5, read=60),  # Use a not-so-long but not not-so-short read timeout
        )

    @staticmethod
    def _build_metabase_field(field, base_type="type/Text"):
        return ["field", field, {"base-type": base_type}]

    @staticmethod
    def _build_metabase_filter(field, values, base_type="type/Text"):
        return [
            "=",
            Client._build_metabase_field(field, base_type),
            *values,
        ]

    @staticmethod
    def _join_metabase_filters(*filters):
        return [
            "and",
            *filters,
        ]

    def build_query(self, *, select=None, table=None, where=None, group_by=None, limit=None):
        query = {}
        if select:
            query["fields"] = [self._build_metabase_field(field) for field in select]
        if table:
            query["source-table"] = table
        if where:
            query["filter"] = [self._build_metabase_filter(field, values) for field, values in where.items()]
        if group_by:
            query["breakout"] = [self._build_metabase_field(field) for field in group_by]
        if limit:
            query["limit"] = limit

        return query

    def merge_query(self, into, query):
        into = copy.deepcopy(into)

        if "fields" in query:
            into.setdefault("fields", [])
            into["fields"].extend(query["fields"])
        if "filter" in query:
            into.setdefault("filter", [])
            into["filter"] = self._join_metabase_filters(into["filter"], query["filter"])
        if "breakout" in query:
            into.setdefault("breakout", [])
            into["breakout"].extend(query["breakout"])
        if "limit" in query:
            into["limit"] = query["limit"]

        return into

    def build_dataset_query(self, *, database, query):
        return {"database": database, "type": "query", "query": query, "parameters": []}

    def fetch_dataset_results(self, query):
        # /!\ Metabase is compiled with hardcoded limit:
        #  - `/dataset` limit to 2_000 rows as it is used to preview query results
        #  - `/dataset/{export-format}` limit to 1_000_000 rows as it is used to download queries results
        data = self._client.post("/dataset/json", data={"query": json.dumps(query)}).raise_for_status().json()
        if type(data) is not list:
            raise Exception(data["error"])
        return data

    def fetch_card_results(self, card, filters=None, group_by=None):
        if not any([filters, group_by]):
            return self._client.post(f"/card/{card}/query/json").raise_for_status().json()

        dataset_query = self._client.get(f"/card/{card}").raise_for_status().json()["dataset_query"]
        dataset_query["query"] = self.merge_query(
            dataset_query["query"],
            self.build_query(where=filters, group_by=group_by),
        )
        return self.fetch_dataset_results(dataset_query)
