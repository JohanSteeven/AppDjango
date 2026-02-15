from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_entrega', 'prioridad', 'completada']
        widgets = {
            'fecha_entrega': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'prioridad': forms.Select(attrs={'class': 'form-control'}),
            'completada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
