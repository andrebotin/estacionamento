from django.shortcuts import render, redirect
from .models import Pessoa, Veiculo, MovRotativo, Mensalista, MovMensalista
from .forms import PessoaForm, VeiculoForm, MovRotativoForm, MensalistaForm, MovMensalistaForm


def home(request):
    context = {'mensagem':'retorno de contexto'}
    return render(request, 'index.html', context)


def listaPessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'listaPessoas.html', data)


def pessoaNovo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('pessoas') 


def pessoaUpdate(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('pessoas')
    else:
        return render(request, 'updatePessoa.html', data)


def pessoaDelete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('pessoas')
    else:
        return render(request, 'deleteConfirm.html', {'obj': pessoa})


def listaVeiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'listaVeiculos.html', data)


def veiculoNovo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('veiculos')


def veiculoUpdate(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('veiculos')
    else:
        return render(request, 'updateVeiculo.html', data)


def veiculoDelete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('veiculos')
    else:
        return render(request, 'deleteConfirm.html', {'obj': veiculo})


def listaMovRotativos(request):
    movRot = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'movRot': movRot, 'form': form}
    return render(request, 'listaMovRotativos.html', data)


def movRotativoNovo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('mov-rot')


def movRotativoUpdate(request, id):
    data = {}
    movRotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=movRotativo)
    data['movRotativo'] = movRotativo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('mov-rot')
    else:
        return render(request, 'updateMovRotativo.html', data)


def movRotativoDelete(request, id):
    movRotativo = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        movRotativo.delete()
        return redirect('mov-rot')
    else:
        return render(request, 'deleteConfirm.html', {'obj': movRotativo})


def listaMensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'listaMensalistas.html', data)


def mensalistaNovo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('mensalistas')


def mensalistaUpdate(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('mensalistas')
    else:
        return render(request, 'updateMensalista.html', data)


def mensalistaDelete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('mensalistas')
    else:
        return render(request, 'deleteConfirm.html', {'obj': mensalista})


def listaMovMensalistas(request):
    movMensal = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'movMensal': movMensal, 'form': form}
    return render(request, 'listaMovMensalistas.html', data)
    

def movMensalNovo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('mov-mensal')


def movMensalUpdate(request, id):
    data = {}
    movMensal = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=movMensal)
    data['movMensal'] = movMensal
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('mov-mensal')
    else:
        return render(request, 'updateMovMensal.html', data)


def movMensalDelete(request, id):
    movMensal = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        movMensal.delete()
        return redirect('mov-mensal')
    else:
        return render(request, 'deleteConfirm.html', {'obj': movMensal})