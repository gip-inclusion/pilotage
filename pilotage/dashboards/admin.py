from django.contrib import admin

from pilotage.dashboards.models import Category, Dashboard


class DashboardAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "metabase_db_id",
        "category",
        "active",
        "com_alert",
        "com_alert_description",
        "com_alert_text",
        "com_alert_link",
    )


admin.site.register(Dashboard, DashboardAdmin)

admin.site.register(Category)
