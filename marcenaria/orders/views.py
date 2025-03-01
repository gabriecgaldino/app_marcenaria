from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import date
from .forms import OrderForm
from .models import Stage, Order

def list_orders_view(request):
    orders = Order.objects.filter(is_active=True)
    return render(request, 'index.html', {'orders': orders})

def create_order_view(request):
    form_order = OrderForm()

    if request.method == 'POST':
        form_order = OrderForm(request.POST or None)

        if form_order.is_valid():
            order = form_order.save()
            order.save()

            init_stage = Stage(
                order = order,
            )

            init_stage.save()

            
            messages.success(request, 'Pedido criado!')
            redirect('/orders/')
        else:
            messages.error(request, 'Erro ao criar pedido, tente novamente!')
            redirect('/orders/')
    
    today = date.today()
    

    return render(request, 'new-order.html', {
                                            'form_order': form_order,
                                            'today': today
                                          })

def delete_order_view(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
        
    if order.is_active:
        order.is_active = False
        order.save()
        messages.success(request, 'Pedido Removido!')

    return redirect('/orders/')


def edit_order_view(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    if request.method == 'POST':
        form_edit = OrderForm(request.POST, instance=order)

        if form_edit.is_valid():
            form_edit.save()

            # Captura a etapa selecionada no formulário
            selected_stage = request.POST.get('order_stage')

            # Atualiza a etapa apenas se for uma seleção válida
            if selected_stage in dict(Stage.STAGE_CHOICE):
                Stage.objects.create(order=order, stage=selected_stage)

            messages.success(request, 'Pedido atualizado!')
            return redirect('/orders/')
        else:
            messages.error(request, 'Verifique os dados informados e tente novamente')

    form_edit = OrderForm(instance=order)
    stages = Stage.STAGE_CHOICE

    return render(request, 'order.html', {'form_edit': form_edit,
                                          'stages': stages,
                                          'order': order})


