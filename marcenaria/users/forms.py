from .models import Users
from django.forms import ModelForm
from django import forms

class LoginForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Usuário',
                'autocomplete': 'off'
            }),
            'password': forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder': 'Senha',
                'autocomplete': 'off'
            })
        }


