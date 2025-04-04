from django.contrib import admin

from reports.models import Report


class ReportAdmin(admin.ModelAdmin):
    list_display = ["__str__", "created_at", "updated_at", "is_ready"]
    readonly_fields = ["created_at", "updated_at"]


admin.site.register(Report, ReportAdmin)
