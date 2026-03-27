from django.contrib import admin
from .models import Event, CalendarDay, CalendarEvent

admin.site.register(Event)
admin.site.register(CalendarDay)
admin.site.register(CalendarEvent)