from django.apps import AppConfig
from django.core.checks import Tags, register

from pilotage.itoutils.checks import check_verbose_name_lower


class ITOUtilsAppConfig(AppConfig):
    name = "pilotage.itoutils"
    verbose_name = "ITOUtils"

    def ready(self):
        super().ready()
        register(Tags.models)(check_verbose_name_lower)
