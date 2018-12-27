#planner/models.py
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    due_date = models.DateField(blank=True, null=True)