from django.db import models
from django.utils import timezone


class Group(models.Model):
    group_number = models.CharField(max_length=20)

    def __str__(self):
        return self.group_number


class ScheduleChanges(models.Model):
    schedule = models.FileField(upload_to="uploads/shedules")
    publication_date = models.DateTimeField(default=timezone.now)

    group_number = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_number.group_number
