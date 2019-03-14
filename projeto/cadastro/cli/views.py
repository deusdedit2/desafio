from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required


# Create your views here.

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','telefone','cep','endereco','numero','cidade','estado','pais']



@login_required(login_url='/contas/login/')
def cliente_list(request, template_name='cliente_list.html'):
    cliente = Cliente.objects.all()
    clientes = {'lista': cliente}
    return render(request, template_name, clientes)

@login_required(login_url='/contas/login/')
def cliente_new(request, template_name='cliente_form.html'):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clientes:listar_clientes')
    return render(request, template_name, {'form': form})


@login_required(login_url='/contas/login/')
def cliente_edit(request, pk, template_name='cliente_form.html'):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save()
            return redirect('clientes:listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, template_name, {'form': form})


@login_required(login_url='/contas/login/')
def cliente_remove(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    if request.method == "POST":
        cliente.delete()
        return redirect('clientes:listar_clientes')
    return render(request, 'cliente_delete.html', {'cliente': cliente})