from django.urls import path
from .models import FilterVote
from .views import *

urlpatterns = [
    path("", VoteListView.as_view(),name="list-vote"),
    # path("<int:pk>/", VoteListView.as_view(),name="voting-page"),
]

app_name = "votes"