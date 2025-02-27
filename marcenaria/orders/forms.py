from .models import Order, Stage
from django.forms import ModelForm

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['order_number', 'customer_name', 'product_name', 'description', 'term']
