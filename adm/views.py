from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from adm.models import Cliente, Carro, Serviço, Peça
from adm.forms import ClienteForm, CarroForm, ServicoForm, PecaForm
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
    clienteform = Cliente()
    carroform_inline = inlineformset_factory(Cliente, Carro, form = CarroForm, extra=1, can_delete=False)
    
    if request.method == 'POST':
        cliente = ClienteForm(request.POST, instance=clienteform)
        carro = carroform_inline(request.POST, instance=clienteform)
        
        if cliente.is_valid() and carro.is_valid():
            cliente = cliente.save(commit=False)
            cliente.save()
            carro.save()
            return HttpResponseRedirect(reverse('listaclientes')) 
        
        else:
            cliente = ClienteForm(instance=clienteform)
            carro = carroform_inline(instance=clienteform)
            return render(request, 'novocliente.html', {'cliente':cliente, 'carro':carro})
    
    else:
        cliente = ClienteForm(instance=clienteform)
        carro = carroform_inline(instance=clienteform)
        return render(request, 'novocliente.html', {'cliente':cliente, 'carro':carro})
        
def editarcliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    formcliente = ClienteForm(instance=cliente)
    
    if request.method == 'POST':
        formcliente = ClienteForm(request.POST, instance=cliente)
        
        if formcliente.is_valid():
            cliente.save()
            return HttpResponseRedirect(reverse('listacarros'))
            
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
    formcarro = CarroForm(instance=carro)
    
    if request.method == 'POST':
        formcarro = CarroForm(request.POST, instance=carro)
        
        if formcarro.is_valid():
            carro.save()
            return HttpResponseRedirect(reverse('listacarros', args=[carro.cliente.id]))    
        else:
            return render(request, 'editarcarro.html', {'carro':carro, 'formcarro':formcarro}) 
    else:
        return render(request, 'editarcarro.html', {'carro':carro, 'formcarro':formcarro}) 
        
def adicionarcarro(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    carroform = Carro()
    servicoform_inline = inlineformset_factory(Carro, Serviço, form = ServicoForm, extra=1, can_delete=False)
    if request.method == 'POST':
        formcarro = CarroForm(request.POST, instance= carroform)
        servico = servicoform_inline(request.POST, instance=carroform)
        
        if formcarro.is_valid() and servico.is_valid():
            carro = formcarro.save(commit=False)
            carro.cliente = cliente
            carro.save()
            servico.save()
            return HttpResponseRedirect(reverse('listacarros', args=[carro.cliente.id]))  
        
        else:
            formcarro = CarroForm()
            servico = servicoform_inline(instance=carroform)
            return render(request, 'adicionarcarro.html', {'carro' : formcarro, 'servico':servico})
    else:
        formcarro = CarroForm()
        servico = servicoform_inline(instance=carroform)
        return render(request, 'adicionarcarro.html', {'carro' : formcarro, 'servico':servico})
    
            
def deletecarro(request, id):
    carro = get_object_or_404(Carro, pk=id)
    carro.delete()
    return HttpResponseRedirect(reverse('listacarros', args=[carro.cliente.id])) 
    
def novoservico(request, id):
    carro = get_object_or_404(Carro, pk=id)
    if request.method == 'POST':
        formservico = ServicoForm(request.POST)
       
        if formservico.is_valid():
            servico = formservico.save(commit=False)
            servico.carro = carro
            servico.save()
            return HttpResponseRedirect(reverse('listaservico', args=[servico.carro.id])) 
        
        else:
            formservico = ServicoForm()
            return render(request, 'novoservico.html', {'servico' : formservico})
    else:
        formservico = ServicoForm()
        return render(request, 'novoservico.html', {'servico' : formservico})
        
def listaservico(request, id):
    carro = get_object_or_404(Carro, pk=id)
    return render(request, 'listaservico.html', {'carro':carro}) 

def editarservico(request, id):
    servico = get_object_or_404(Serviço, pk=id)
    formservico = ServicoForm(instance=servico)
    if request.method == 'POST':
        formservico = ServicoForm(request.POST, instance=servico)
        if formservico.is_valid():
            servico.save()
            return HttpResponseRedirect(reverse('listaservico', args=[servico.carro.id]))
        else:
            return render(request, 'editarservico.html', {'formservico': formservico})
    else:
        return render(request, 'editarservico.html', {'formservico':formservico})
        
def deleteservico(request, id):
    servico = get_object_or_404(Serviço, pk=id)
    servico.delete()
    return HttpResponseRedirect(reverse('listaservico', args=[servico.carro.id]))

