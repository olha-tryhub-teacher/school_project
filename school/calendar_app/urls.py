from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name='calendar'),
    path('date/<str:date>/', views.events_by_date, name='events_by_date'),
]