from django import forms
from bikes.models import Bikes
from datetime import datetime

class BikesForms(forms.ModelForm):
    class Meta:
        model = Bikes
        exclude = ['publicada', ]
        labels = {
            'descricao': 'Descrição',
            'data_fotografia': 'Data de registro',
            'usuarios': 'Usuário',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'cor': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'categoria': forms.Select(attrs={'class': 'form-control mb-3'}),
            'preco': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'ano': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'foto': forms.FileInput(attrs={'type': "file", 'class': "form-control-file mt-3", 'id': "foto", 'name': "foto",
            'accept': "image/*", 'onchange': "previewImage(this)"}),
            'data_fotografia': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'value': datetime.now().strftime("%d/%m/%Y")}),
            'usuarios': forms.Select(attrs={'class': 'form-control'}),
        }

