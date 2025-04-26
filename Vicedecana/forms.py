from django import forms
from .models import Estudiantes, Edificios  # Apartamentos eliminado

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Nombre Completo'}),
            'usuario': forms.TextInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Usuario'}),
            'id': forms.TextInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Solapín'}),
            'grade': forms.NumberInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Año'}),
            'carrera': forms.TextInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Carrera'}),
            'province': forms.TextInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Provincia'}),
            'municipio': forms.TextInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Municipio'}),
            'facultad': forms.Select(
                attrs={
                    'class': 'col-md-6 form-control',
                },
                choices=[
                    ('Facultad 1', 'Facultad 1'), ('Facultad 2', 'Facultad 2'),
                    ('Facultad 3', 'Facultad 3'), ('Facultad 4', 'Facultad 4'),
                    ('FTE', 'FTE'), ('CITEC', 'CITEC')
                ]
            ),
        }


class EdificioForm(forms.ModelForm):
    class Meta:
        model = Edificios
        fields = '__all__'
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Numero'}),
            'disponibilidad': forms.TextInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Disponibilidad'}),
            'ano': forms.NumberInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Año'}),
            'carrera': forms.TextInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Carrera'}),
            'facultad': forms.Select(
                attrs={
                    'class': 'col-md-6 form-control',
                },
                choices=[
                    ('Facultad 1', 'Facultad 1'), ('Facultad 2', 'Facultad 2'),
                    ('Facultad 3', 'Facultad 3'), ('Facultad 4', 'Facultad 4'),
                    ('FTE', 'FTE'), ('CITEC', 'CITEC')
                ]
            ),
        }
