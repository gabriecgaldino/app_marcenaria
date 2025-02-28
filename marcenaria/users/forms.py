from .models import Users
from django.forms import ModelForm
from django import forms

class LoginForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder':'Usuário',
                'class': 'form-control'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Senha',
                'class': 'form-control'
            })
        }


