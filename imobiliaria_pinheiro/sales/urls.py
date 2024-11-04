from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.index, name='index'),
    path('cadastrar/', views.cadastrar_imovel, name='cadastrar_imovel'),
]
