from django.contrib import admin
from django.db import transaction
from django.shortcuts import redirect
from django.urls import path, reverse

from reports.models import Report
from reports.tasks import generate_report_task


class ReportAdmin(admin.ModelAdmin):
    list_display = ["__str__", "created_at", "updated_at", "is_ready"]
    change_list_template = "admin/reports/report/change_list.html"
    readonly_fields = ["created_at", "updated_at"]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "generate/",
                self.admin_site.admin_view(self.admin_generate_report_view),
                name="reports_generate",
            ),
        ]
        return custom_urls + urls

    def admin_generate_report_view(self, request):
        with transaction.atomic():
            report = Report.objects.create()

        redirect_url = reverse("admin:reports_report_change", kwargs={"object_id": report.id})
        result = generate_report_task.delay(report_id=report.id, redirect_url=redirect_url)

        self.message_user(request, "Started generating a report...")
        return redirect("admin:task_status", result.id)


admin.site.register(Report, ReportAdmin)
