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
    # 🔥 Agregamos el nuevo campo Apartamento
    apartamento = forms.ChoiceField(
        choices=[
            ('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'),
            ('106', '106'), ('107', '107'), ('108', '108'), ('109', '109'), ('110', '110'),
            ('201', '201'), ('202', '202'), ('203', '203'), ('204', '204'), ('205', '205'),
            ('206', '206'), ('207', '207'), ('208', '208'),
            ('301', '301'), ('302', '302'), ('303', '303'), ('304', '304'), ('305', '305'),
            ('306', '306'), ('307', '307'), ('308', '308')
        ],
        widget=forms.Select(attrs={'class': 'col-md-6 form-control'}),
        required=True,
        label="Apartamento"
    )

    class Meta:
        model = Edificios
        fields = '__all__'  # 🔥 De momento, mantenemos todos los campos + apartamento manual
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Número del edificio'}),
            'disponibilidad': forms.TextInput(attrs={'class': 'col-md-6 form-control', 'placeholder': 'Disponibilidad'}),
            'ano': forms.Select(
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
