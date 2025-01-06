from django.db import models


class Event(models.Model):
    events_title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pk} ({self.events_title})"
