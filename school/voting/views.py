from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView

from .models import Vote


# Create your views here.

class VoteListView(ListView):
    model = Vote
    context_object_name = 'votes'
    template_name = 'voting_temp/vote_list.html'


