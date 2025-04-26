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
            'grade': forms.Select(   # 🔥 cambiado a Select
                attrs={'class': 'col-md-6 form-control'},
                choices=[
                    ('1', '1ro'),
                    ('2', '2do'),
                    ('3', '3ro'),
                    ('4', '4to'),
                ]
            ),
            'carrera': forms.Select(
                attrs={'class': 'col-md-6 form-control'},
                choices=[
                    ('ICI', 'Ingeniería Informática (ICI)'),
                    ('BIO', 'Ingeniería en Bioinformática (BIO)'),
                    ('CIBER', 'Ciberseguridad (CIBER)'),
                ]
            ),
            'province': forms.TextInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Provincia'}),
            'municipio': forms.TextInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Municipio'}),
            'facultad': forms.Select(
                attrs={'class': 'col-md-6 form-control'},
                choices=[
                    ('FTI', 'FTI'), ('FCS', 'FCS'),
                    ('FIO', 'FIO'), ('FTL', 'FTL'),
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
            'ano': forms.Select(   # 🔥 cambiado a Select
                attrs={'class': 'col-md-6 form-control'},
                choices=[
                    ('1', '1ro'),
                    ('2', '2do'),
                    ('3', '3ro'),
                    ('4', '4to'),
                ]
            ),
            'carrera': forms.Select(
                attrs={'class': 'col-md-6 form-control'},
                choices=[
                    ('ICI', 'Ingeniería Informática (ICI)'),
                    ('BIO', 'Ingeniería en Bioinformática (BIO)'),
                    ('CIBER', 'Ciberseguridad (CIBER)'),
                ]
            ),
            'facultad': forms.Select(
                attrs={'class': 'col-md-6 form-control'},
                choices=[
                    ('FTI', 'FTI'), ('FCS', 'FCS'),
                    ('FIO', 'FIO'), ('FTL', 'FTL'),
                    ('FTE', 'FTE'), ('CITEC', 'CITEC')
                ]
            ),
        }
