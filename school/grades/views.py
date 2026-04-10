from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from school_project.school.grades import models


# Create your views here.
class SubjectListView(ListView):
    model = models.Subject
    context_object_name = 'subject_list'
    template_name = 'grades/subject_list.html'

