from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrderForm
from .models import Stage, Order

def create_order_view(request):
    form_order = OrderForm()

    if request.method == 'POST':
        form_order = OrderForm(request.POST or None)

        if form_order.is_valid():
            order = form_order.save()
            order.save()

            init_stage = Stage(
                order_number = order.order_number,
            )
            
            init_stage.save()
            messages.success(request, 'Pedido criado!')
        else:
            messages.error(request, 'Erro ao criar pedido, tente novamente!')
            redirect('/')
    if request.method == 'GET':
        orders = Order.objects.all()

    return render(request, 'index.html', {'form_order': form_order,
                                          'orders': orders})
