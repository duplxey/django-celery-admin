from celery.result import AsyncResult
from django.contrib import admin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import path


class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "task-status/<str:task_id>/",
                self.admin_view(self.admin_task_status_view),
                name="task_status",
            )
        ]
        return custom_urls + urls

    def admin_task_status_view(self, request, task_id):
        task = AsyncResult(task_id)
        task_data = {
            "id": task.id,
            "name": task.name,
            "args": task.args,
            "kwargs": task.kwargs,
            "state": task.state,
        }

        # Return JSON response if requested
        if request.headers.get("Accept", "").startswith("application/json"):
            return JsonResponse(task_data)

        # Otherwise, render HTML response
        return render(
            request,
            "admin/task_status.html",
            {
                "title": "Task Status",
                "task": task_data,
            },
        )
