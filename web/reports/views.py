import time

from django.http import JsonResponse

from reports.models import Report


def generate_report(request):
    report = Report.objects.create()

    # Simulate a long-running report generation
    time.sleep(15)
    report.content = "This report was generated synchronously."
    report.is_ready = True
    report.save()

    return JsonResponse({
        "status": "The report has been successfully generated!",
    })
