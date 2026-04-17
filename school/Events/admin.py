from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'location', 'created_by')
    search_fields = ('title', 'description')
    list_filter = ('start_date', 'created_by')
