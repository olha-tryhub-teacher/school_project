from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm

class EventListView(ListView):
    model = Event
    template_name = 'Events/event_list.html'
    context_object_name = 'events'
    ordering = ['-start_date']

class EventDetailView(DetailView):
    model = Event
    template_name = 'Events/event_detail.html'
    context_object_name = 'event'

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'Events/event_form.html'
    success_url = reverse_lazy('event_list')

    def form_valid(self, form):
        from django.contrib.auth.models import User

        default_user = User.objects.first()

        if default_user:
            form.instance.created_by = default_user
            return super().form_valid(form)
        else:
            from django.core.exceptions import ValidationError
            form.add_error(None,
                           "Помилка: У базі даних немає жодного користувача. Створіть суперкористувача через термінал!")
            return self.form_invalid(form)

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'Events/event_form.html'
    success_url = reverse_lazy('event_list')

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'Events/event_confirm_delete.html'
    success_url = reverse_lazy('event_list')