from django.shortcuts import render
from .models import CalendarDay, CalendarEvent

def calendar_view(request):
    days = CalendarDay.objects.all()
    return render(request, 'calendar.html', {'days': days})


def events_by_date(request, date):
    events = CalendarEvent.objects.filter(date__exact=date)

    return render(request, 'events.html', {
        'events': events,
        'date': date
    })