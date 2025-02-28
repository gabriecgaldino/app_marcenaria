from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import date
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
                order_number = order,
            )
            
            init_stage.save()
            messages.success(request, 'Pedido criado!')
            return redirect('/orders/')
        else:
            messages.error(request, 'Erro ao criar pedido, tente novamente!')
            redirect('/pedidos/')
    orders = Order.objects.all()
    today = date.today()

    return render(request, 'index.html', {'form_order': form_order,
                                          'orders': orders,
                                          'today': today
                                          })

def delete_order_view(request, order_number):
        order = get_object_or_404(Order, order_number=order_number)
        order.delete()
        messages.success(request, 'Pedido Removido!')
        return redirect('/orders/')


def edit_order_view(request, order_number):
     return


