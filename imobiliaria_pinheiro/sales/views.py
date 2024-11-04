# views.py
from django.shortcuts import render, redirect
from .models import Imovel
from .forms import ImovelForm

def index(request):
    return render(request, 'sales/index.html')

def home(request):
    imoveis = Imovel.objects.all()
    return render(request, 'home.html', {'imoveis': imoveis})

def cadastrar_imovel(request):
    if request.method == 'POST':
        form = ImovelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImovelForm()
    return render(request, 'cadastro.html', {'form': form})
