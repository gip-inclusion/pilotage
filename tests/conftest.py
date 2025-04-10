import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(config, items):
    """Automatically add pytest db marker if needed."""
    for item in items:
        markers = {marker.name for marker in item.iter_markers()}
        if "no_django_db" not in markers and "django_db" not in markers:
            item.add_marker(pytest.mark.django_db)


@pytest.fixture(name="default_settings", autouse=True)
def default_settings_fixture(settings):
    settings.METABASE_BASE_URL = "https://metabase.fake"
    settings.METABASE_API_KEY = ""
