from django import forms
from .models import Imovel

class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = ['titulo', 'preco', 'descricao', 'imagem']

