from django import forms
from .models import Estudiantes, Edificios, Apartamento

PROVINCIAS_CUBA = [
    ('Pinar del Río', 'Pinar del Río'),
    ('Artemisa', 'Artemisa'),
    ('La Habana', 'La Habana'),
    ('Mayabeque', 'Mayabeque'),
    ('Matanzas', 'Matanzas'),
    ('Cienfuegos', 'Cienfuegos'),
    ('Villa Clara', 'Villa Clara'),
    ('Sancti Spíritus', 'Sancti Spíritus'),
    ('Ciego de Ávila', 'Ciego de Ávila'),
    ('Camagüey', 'Camagüey'),
    ('Las Tunas', 'Las Tunas'),
    ('Holguín', 'Holguín'),
    ('Granma', 'Granma'),
    ('Santiago de Cuba', 'Santiago de Cuba'),
    ('Guantánamo', 'Guantánamo'),
    ('Isla de la Juventud', 'Isla de la Juventud'),
]

class EstudianteForm(forms.ModelForm):
    edificio = forms.ModelChoiceField(
        queryset=Edificios.objects.all(),
        empty_label="Seleccione Edificio",
        widget=forms.Select(attrs={'class': 'col-md-6 form-control'})
    )

    class Meta:
        model = Estudiantes
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Nombre Completo'}),
            'usuario': forms.TextInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Usuario'}),
            'id': forms.TextInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Solapín'}),
            'grade': forms.Select(
                attrs={'class': 'col-md-6 form-control'},
                choices=[('', 'Seleccione Año'), ('1', '1ro'), ('2', '2do'), ('3', '3ro'), ('4', '4to')]
            ),
            'carrera': forms.Select(
                attrs={'class': 'col-md-6 form-control'},
                choices=[('', 'Seleccione Carrera'), 
                         ('ICI', 'Ingeniería Informática (ICI)'),
                         ('BIO', 'Ingeniería en Bioinformática (BIO)'),
                         ('CIBER', 'Ciberseguridad (CIBER)')]
            ),
            'province': forms.Select(
                attrs={'class': 'col-md-6 form-control'},
                choices=[('', 'Seleccione Provincia')] + PROVINCIAS_CUBA,
            ),
            'municipio': forms.TextInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Municipio'}),
            'facultad': forms.Select(
                attrs={'class': 'col-md-6 form-control'},
                choices=[('', 'Seleccione Facultad'), 
                         ('FTI', 'FTI'), ('FCS', 'FCS'),
                         ('FIO', 'FIO'), ('FTL', 'FTL'),
                         ('FTE', 'FTE'), ('CITEC', 'CITEC')]
            ),
            'apartamento': forms.Select(attrs={'class': 'col-md-6 form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['apartamento'].empty_label = "Seleccione Apartamento"



class EdificioForm(forms.ModelForm):
    cantidad_apartamentos = forms.IntegerField(
        min_value=1,
        max_value=100,
        required=True,
        label="Cantidad de Apartamentos",
        widget=forms.NumberInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Ej: 8, 10, 20'})
    )

    class Meta:
        model = Edificios
        fields = ['numero', 'facultad', 'disponibilidad', 'ano', 'carrera']
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Número del edificio'}),
            'disponibilidad': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ano': forms.Select(
                attrs={'class': 'col-md-6 form-control'},
                choices=[('', 'Seleccione Año'), ('1', '1ro'), ('2', '2do'), ('3', '3ro'), ('4', '4to')]
            ),
            'carrera': forms.Select(
                attrs={'class': 'col-md-6 form-control'},
                choices=[('', 'Seleccione Carrera'),
                         ('ICI', 'Ingeniería Informática (ICI)'),
                         ('BIO', 'Ingeniería en Bioinformática (BIO)'),
                         ('CIBER', 'Ciberseguridad (CIBER)')]
            ),
            'facultad': forms.Select(
                attrs={'class': 'col-md-6 form-control'},
                choices=[('', 'Seleccione Facultad'),
                         ('FTI', 'FTI'), ('FCS', 'FCS'),
                         ('FIO', 'FIO'), ('FTL', 'FTL'),
                         ('FTE', 'FTE'), ('CITEC', 'CITEC')]
            ),
        }

