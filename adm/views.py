from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from adm.models import Cliente, Carro, Serviço
from adm.forms import ClienteFormset, CarroFormset, ServicoFormSet
from django.urls import reverse
from django.forms import inlineformset_factory

def home(request):
    return render(request, 'base.html')

def listaclientes(request):
    clientes = Cliente.objects.all().order_by('-created_at')
    return render(request, 'listaclientes.html', {'clientes' : clientes})

def listacarros(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    return render(request, 'listacarros.html', {'cliente':cliente})

def novocliente(request):
    if request.method == 'POST':
        clienteform = ClienteFormset(request.POST)
        carroform = CarroFormset(request.POST)
        
        if clienteform.is_valid() and carroform.is_valid():
            cliente = clienteform.save()
            carro = carroform.save(commit=False)
            carro.cliente = cliente
            carro.save()
            return redirect('/listaclientes/')
        
        else:
            return render(request, 'novocliente.html', {'cliente': clienteform, 'carro':carroform})
        
    else:
        clienteform = ClienteFormset()
        carroform = CarroFormset()
        return render(request, 'novocliente.html', {'cliente' : clienteform, 'carro':carroform})
    

def editarcliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    formcliente = ClienteFormset(instance=cliente)
    
    if request.method == 'POST':
        formcliente = ClienteFormset(request.POST, instance=cliente)
        
        if formcliente.is_valid():
            cliente.save()
            return redirect('/listaclientes/')
            
        else:
            return render(request, 'editarcliente.html', {'cliente':cliente, 'formcliente':formcliente})
    
    else:
        return render(request, 'editarcliente.html', {'cliente':cliente, 'formcliente':formcliente})
        
def deletecliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    return redirect('/listaclientes/')

def editarcarro(request, id):
    carro = get_object_or_404(Carro, pk=id)
    formcarro = CarroFormset(instance=carro)
    
    if request.method == 'POST':
        formcarro = CarroFormset(request.POST, instance=carro)
        
        if formcarro.is_valid():
            carro.save()
            return HttpResponseRedirect(reverse('listacarros', args=[carro.cliente.id]))    
        else:
            return render(request, 'editarcarro.html', {'carro':carro, 'formcarro':formcarro}) 
    else:
            return render(request, 'editarcarro.html', {'carro':carro, 'formcarro':formcarro}) 
        
def adicionarcarro(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == 'POST':
        formcarro = CarroFormset(request.POST)
        if formcarro.is_valid():
            carro = formcarro.save(commit=False)
            carro.cliente = cliente
            carro.save()
            return HttpResponseRedirect(reverse('listacarros', args=[carro.cliente.id]))  
        
        else:
            return render(request, 'adicionarcarro.html', {'carro' : formcarro})
    else:
        formcarro = CarroFormset()
        
        return render(request, 'adicionarcarro.html', {'carro' : formcarro})
    
            
def deletecarro(request, id):
    carro = get_object_or_404(Carro, pk=id)
    carro.delete()
    return HttpResponseRedirect(reverse('listacarros', args=[carro.cliente.id])) 
    
def novoservico(request, id):
    carro = get_object_or_404(Carro, pk=id)
    if request.method == 'POST':
        formservico = ServicoFormSet(request.POST)
        if formservico.is_valid():
            servicos = formservico.save(commit=False)
            for servico in servicos:
                servico.carro = carro
                servico.save()
            return HttpResponseRedirect(reverse('listaservico', args=[servico.carro.id])) 
        else:
            return render(request, 'novoservico.html', {'servico' : formservico})
    else:
        formservico = ServicoFormSet()
        return render(request, 'novoservico.html', {'servico' : formservico})
        
def listaservico(request, id):
    carro = get_object_or_404(Carro, pk=id)
    return render(request, 'listaservico.html', {'carro':carro}) 

def editarservico(request, id):
    servico = get_object_or_404(Serviço, pk=id)
    formservico = ServicoFormSet()
    if request.method == 'POST':
        formservico = ServicoFormSet(request.POST)
        if formservico.is_valid():
            servico.save()
            return HttpResponseRedirect(reverse('listaservico', args=[servico.carro.id]))
        else:
            return render(request, 'editarservico.html', {'formservico': formservico})
    else:
        formservico = ServicoFormSet()
        return render(request, 'editarservico.html', {'formservico':formservico})
        
