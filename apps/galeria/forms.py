from django import forms
from apps.galeria.models import Fotografia


class FotografiaForm(forms.ModelForm): 
    class Meta:
        model = Fotografia
        exclude = ['publicada',]

        labels = {
            'nome': 'Nome da Fotografia',
            'legenda': 'Legenda da Fotografia',
            'categoria': 'Categoria da Fotografia',
            'descricao': 'Descrição da Fotografia',
            'foto': 'Foto',
            'data_fotografia': 'Data da Fotografia',
            'usuario': 'Usuário',
        }
        
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control',}),
            'legenda': forms.TextInput(attrs={'class':'form-control',}),
            'categoria': forms.Select(attrs={'class':'form-control',}),
            'descricao': forms.Textarea(attrs={'class':'form-control',}),
            'foto': forms.FileInput(attrs={'class':'form-control',}),
            'data_fotografia': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'}),
            'usuario': forms.Select(attrs={'class':'form-control',}),
        }
#essa classe usa o model Fotografia e define quais campos do model 
#serão exibidos no formulário de cadastro de fotografias.