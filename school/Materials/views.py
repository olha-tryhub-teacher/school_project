from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Material

#Список матеріалів
class MaterialListView(ListView):
    model = Material
    template_name = 'materials/material_list.html'
    context_object_name = 'materials'
    ordering = ['-created_at']
    paginate_by = 5

#Сторінка одного матеріалу
class MaterialDetailView(DetailView):
    model = Material
    template_name = 'materials/material_detail.html'
    context_object_name = 'material'

#Завантаження матеріалу
class MaterialCreateView(LoginRequiredMixin, CreateView):
    model = Material
    template_name = 'materials/material_form.html'
    fields = ['title', 'description', 'file', 'link', 'youtube_url', 'material_type']
    success_url = reverse_lazy('material_list')

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)