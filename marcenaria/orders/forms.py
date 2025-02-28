from django import forms
from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'product_name', 'description', 'term']
        widgets = {
            'term': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            })
        }

    # Adicionando classes aos campos manualmente, caso necessário
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['customer_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nome do Cliente',
            'disabled': True
        })
        self.fields['product_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nome do Produto',
            'disabled': True
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Descrição do Produto',
            'rows': 3,
            'disabled': True
        })
        self.fields['term'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Data do Pedido',
            'disabled': True
        })

