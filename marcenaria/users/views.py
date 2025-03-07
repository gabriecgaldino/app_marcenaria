from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    print(request.POST)
    form = LoginForm(request.POST or None, data=request.POST)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Usuário conectado')
                return redirect('/orders/')
            else:
                messages.warning(request, 'Usuário não encontrado ou senha incorreta')
        else:
            print("Erros do formulário:", form.errors)
            messages.error(request, 'Por favor, corrija os erros no formulário.')

    return render(request, 'login.html', {'form': form})

