from django.shortcuts import render, redirect
from .models import CalendarDay, CalendarEvent
from django.views.generic import ListView

class CalendarEventListView(ListView):
    model = CalendarEvent
    template_name = 'calendar_event_list.html'
    context_object_name = 'events'
    paginate_by = 10

def calendar_view(request):
    visits = request.session.get('visits', 0)
    request.session['visits'] = visits + 1

    days = CalendarDay.objects.all()
    return render(request, 'calendar.html', {
        'days': days,
        'visits': visits + 1
    })

def reset_visits(request):
    request.session['visits'] = 0
    return redirect('calendar')

def events_by_date(request, date):
    events = CalendarEvent.objects.filter(date__exact=date)

    return render(request, 'events.html', {
        'events': events,
        'date': date
    })

from .forms import CalendarEventForm
from django.shortcuts import redirect

def add_event(request):
    if request.method == 'POST':
        form = CalendarEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
        else:
            print(form.errors)
    else:
        form = CalendarEventForm()

    return render(request, 'add_event.html', {'form': form})