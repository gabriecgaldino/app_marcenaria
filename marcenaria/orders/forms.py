from .models import Order, Stage
from django.forms import ModelForm
from django import forms

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'product_name', 'description', 'term']
        widgets = {
            'term': forms.DateInput(attrs={
                'type':'date'
            })
        }
