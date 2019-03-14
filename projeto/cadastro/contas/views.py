from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #loga o usuario
            login(request,user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('clientes:listar_clientes')
    else:
      form = UserCreationForm()
    return render(request, 'contas/cadastrar.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #loga o usuario
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('clientes:listar_clientes')
    else:
        form = AuthenticationForm()
    return render(request, 'contas/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('clientes:listar_clientes')