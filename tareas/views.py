from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Tarea
from .forms import TareaForm

class TareaListView(ListView):
    model = Tarea
    template_name = 'tareas/tarea_list.html'
    context_object_name = 'tareas'
    ordering = ['fecha_entrega']

class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tareas/tarea_detail.html'
    context_object_name = 'tarea'

class TareaCreateView(SuccessMessageMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/tarea_form.html'
    success_url = reverse_lazy('tarea-list')
    success_message = "Tarea creada exitosamente."

class TareaUpdateView(SuccessMessageMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/tarea_form.html'
    success_url = reverse_lazy('tarea-list')
    success_message = "Tarea actualizada exitosamente."

class TareaDeleteView(SuccessMessageMixin, DeleteView):
    model = Tarea
    template_name = 'tareas/tarea_confirm_delete.html'
    success_url = reverse_lazy('tarea-list')
    success_message = "Tarea eliminada exitosamente."
    

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
