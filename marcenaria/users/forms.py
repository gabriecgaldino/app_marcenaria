from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Usuário',
            'class': 'form-control',
            'autocomplete': 'off'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Senha',
            'class': 'form-control',
            'autocomplete': 'off'
        })