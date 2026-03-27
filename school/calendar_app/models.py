# Create your models here.

from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class CalendarDay(models.Model):
    date = models.DateField()
    notes = models.TextField(blank=True)

class CalendarEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateField()
