from .models import Users
from django.forms import ModelForm
from django import forms

class LoginForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class':'form-control form-control-lg',
                'placeholder':'Usuário'
            }),
            'password': forms.PasswordInput(attrs={
                'class':'form-control form-control-lg',
                'placeholder': 'Senha'
            })
        }


