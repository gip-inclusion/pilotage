from django.contrib import admin

from dashboards.models import Dashboard


class DashboardAdmin(admin.ModelAdmin):
    list_display = ('title', 'metabase_db_id')

admin.site.register(Dashboard, DashboardAdmin)
