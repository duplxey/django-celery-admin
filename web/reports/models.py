from django.db import models


class Report(models.Model):
    content = models.TextField()
    is_ready = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return f"Report #{self.pk}"
