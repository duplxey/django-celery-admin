import time

from celery import shared_task

from reports.models import Report


@shared_task
def generate_report_task(report_id, **kwargs):
    report = Report.objects.get(id=report_id)

    # Simulate a long-running report generation
    time.sleep(15)
    report.content = "testdriven.io is cool!"
    report.is_ready = True
    report.save()

    return "The report has been successfully generated!"
