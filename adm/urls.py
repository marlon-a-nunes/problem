from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name= 'home'),
    path('listaclientes/', views.listaclientes, name='listaclientes'),
    path('listacarros/<int:id>', views.listacarros, name='listacarros'), 
    path('novocliente/', views.novocliente, name= 'novocliente'),
    path('editarcliente/<int:id>', views.editarcliente, name='editarcliente'),
    path('editarcarro/<int:id>', views.editarcarro, name= 'editarcarro'),
    path('adicionarcarro/<int:id>', views.adicionarcarro, name = 'adicionarcarro'),
    path('deletecliente/<int:id>', views.deletecliente, name='deletecliente'),
    path('deletecarro/<int:id>', views.deletecarro, name='deletecarro'),
    path('novoservico/<int:id>', views.novoservico, name='novoservico'),
    path('listaservico/<int:id>', views.listaservico, name='listaservico'),
    path('editarservico/<int:id>', views.editarservico, name='editarservico'),
    path('deleteservico/<int:id>', views.deleteservico, name = 'deleteservico'),
    
    
]

