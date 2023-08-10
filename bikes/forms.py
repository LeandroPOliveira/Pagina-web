from django import forms

from bikes.models import Bikes


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
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cor': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'preco': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'type': "file", 'class': "form-control-file", 'id': "foto", 'name': "foto",
            'accept': "image/*", 'onchange': "previewImage(this)"}),
            'data_fotografia': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-control'}),
            'usuarios': forms.Select(attrs={'class': 'form-control'}),
        }

