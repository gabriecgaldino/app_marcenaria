from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import date
from .forms import OrderForm, StagePictureForm
from .models import Stage, Order
from users.models import Users

def list_orders_view(request):
    orders = Order.objects.filter(is_active=True)
    user = get_object_or_404(Users, id=request.user.id)

    return render(request, 'index.html', {
        'orders': orders,
        'user': user
        })

def create_order_view(request):
    form_order = OrderForm()
    user = get_object_or_404(Users, id=request.user.id)

    if request.method == 'POST':
        form_order = OrderForm(request.POST or None)

        if form_order.is_valid():
            order = form_order.save()
            order.save()

            init_stage = Stage(
                order = order,
                stage = 'ORC'
            )

            init_stage.save()

            
            messages.success(request, 'Pedido criado!')
            return redirect('/orders/')
        else:
            messages.error(request, 'Erro ao criar pedido, tente novamente!')
            return redirect('/orders/')
    
    today = date.today()
    
    return render(request, 'new-order.html', {
                                            'form_order': form_order,
                                            'today': today,
                                            'user': user
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
    user = get_object_or_404(Users, id=request.user.id)

    if request.method == 'POST':
        form_edit = OrderForm(request.POST, instance=order)

        if form_edit.is_valid():
            form_edit.save()

            selected_stage = request.POST.get('order_stage')

            if selected_stage in dict(Stage.STAGE_CHOICE):
                
                order.stages.filter(status=False).update(status=True)

                
                Stage.objects.create(order=order, stage=selected_stage, status=False)


            messages.success(request, 'Pedido atualizado!')
            return redirect('/orders/')
        else:
            messages.error(request, 'Verifique os dados informados e tente novamente')

    form_edit = OrderForm(instance=order)

    current_stage = order.stages.filter(status=False).first()


    stage_dict = {code: name for code, name in Stage.STAGE_CHOICE}
    stage_keys = list(stage_dict.keys())  

    if current_stage:
        
        current_index = stage_keys.index(current_stage.stage)
        stage_choices = [(code, stage_dict[code]) for code in stage_keys[current_index:]]
    else:
        stage_choices = list(stage_dict.items()) 

    return render(request, 'order.html', {
        'form_edit': form_edit,
        'stages': stage_choices,  
        'order': order,
        'current_stage': current_stage,
        'user': user
    })

def add_stage_photo(request, order_number, stage_id):
    stage = get_object_or_404(Stage, id=stage_id)
    order = get_object_or_404(Order, order_number=order_number)
    user = get_object_or_404(Users, id=request.user.id)

    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']  

        stage.pictures = image

        stage.save()

        return redirect('update_stage', order_number=order_number, stage_id=stage_id)
    else:
        form = StagePictureForm()

    return render(request, 'add-picture.html', {'form': form,
                                                'stage': stage,
                                                'order': order,
                                                'user': user
                                                })

