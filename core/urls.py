from django.urls import path

from .views import (
    home, 
    listaPessoas, 
    listaVeiculos, 
    listaMovRotativos,
    listaMensalistas,
    listaMovMensalistas,
    pessoaNovo,
    veiculoNovo,
    movRotativoNovo,
    mensalistaNovo,
    movMensalNovo,
    pessoaUpdate,
    veiculoUpdate,
    movMensalUpdate,
    mensalistaUpdate,
    movRotativoUpdate,
    pessoaDelete,
    veiculoDelete,
    mensalistaDelete,
    movMensalDelete,
    movRotativoDelete,
) 


urlpatterns = [
    path('', home, name='home'),

    path('pessoas/', listaPessoas, name='pessoas'),
    path('pessoa-novo/', pessoaNovo, name='pessoa-novo'),
    path('pessoa-update/<int:id>', pessoaUpdate, name='pessoa-update'),
    path('pessoa-delete/<int:id>', pessoaDelete, name='pessoa-delete'),

    path('veiculos/', listaVeiculos, name='veiculos'),
    path('veiculo-novo/', veiculoNovo, name='veiculo-novo'),
    path('veiculo-update/<int:id>', veiculoUpdate, name='veiculo-update'),
    path('veiculo-delete/<int:id>', veiculoDelete, name='veiculo-delete'),

    path('mov-rot/', listaMovRotativos, name='mov-rot'),
    path('mov-rot-novo/', movRotativoNovo, name='mov-rot-novo'),
    path('mov-rot-update/<int:id>', movRotativoUpdate, name='mov-rot-update'),
    path('mov-rot-delete/<int:id>', movRotativoDelete, name='mov-rot-delete'),

    path('mensalistas/', listaMensalistas, name='mensalistas'),
    path('mensalista-novo/', mensalistaNovo, name='mensalista-novo'),
    path('mensalista-update/<int:id>', mensalistaUpdate, name='mensalista-update'),
    path('mensalista-delete/<int:id>', mensalistaDelete, name='mensalista-delete'),

    path('mov-mensal/', listaMovMensalistas, name='mov-mensal'),
    path('mov-mensal-novo/', movMensalNovo, name='mov-mensal-novo'),
    path('mov-mensal-update/<int:id>', movMensalUpdate, name='mov-mensal-update'),
    path('mov-mensal-delete/<int:id>', movMensalDelete, name='mov-mensal-delete'),

]