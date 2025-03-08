from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from .models import Users

def login_view(request):
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
            messages.error(request, 'Por favor, corrija os erros no formulário.')

    return render(request, 'login.html', {'form': form})

def profile_view(request):
    user = get_object_or_404(Users, id=request.user.id)

    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        user.profile_image = image
        
        user.save()
        messages.success(request, 'Perfil atualizado com sucesso!')
        return redirect('profile')
        

    return render(request, 'profile.html', {'user': user})

