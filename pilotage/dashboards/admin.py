from django.contrib import admin

from dashboards.models import Category, Dashboard


class DashboardAdmin(admin.ModelAdmin):
    list_display = ("title", "metabase_db_id", "category", "active")


admin.site.register(Dashboard, DashboardAdmin)

admin.site.register(Category)
