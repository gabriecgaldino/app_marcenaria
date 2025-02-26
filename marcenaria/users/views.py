from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST or None)

        

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, 'Usuário conectado')
            else:
                messages.warning(request, 'Usuário não está cadastrado')
                
        
    return render(request, 'login.html', {'form': form})
