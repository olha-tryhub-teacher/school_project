from django.urls import path
from . import views
from .views import CalendarEventListView

urlpatterns = [
    path('', views.calendar_view, name='calendar'),
    path('date/<str:date>/', views.events_by_date, name='events_by_date'),
    path('events/', CalendarEventListView.as_view(), name='event_list'),
    path('reset/', views.reset_visits, name='reset_visits'),
    path('add/', views.add_event, name='add_event'),
]