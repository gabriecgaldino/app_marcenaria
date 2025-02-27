from django.db import models
from datetime import datetime

def upload_path(instance, filename):
    return f'orders/{instance.orders.id}/{instance.stage}/{filename}'

class Order(models.Model):
    order_number = models.CharField(max_length=10, unique=True, blank=False, null=False)
    customer_name = models.CharField(max_length=50, blank=False, null=False)
    product_name = models.CharField(max_length=50, blank=False, null=False)
    status = models.BooleanField(default=False)
    description = models.TextField(max_length=350)
    term = models.DateField(blank=False, null=False)
    created_At = models.DateField(default=datetime.today(), blank=False, null=False)
    updated_At = models.DateField(max_length=datetime.today())

    def save(self, *args, **kwargs):
        if not self.order_number:
            last_order = Order.objects.order_by('-created_At').first()
            if last_order:
                last_number = int(last_order.order_number[:3])
                self.order_number = f'ORD{last_number + 1:06d}'
            else:
                self.order_number = 'ORD000001'
        super().save(*args, **kwargs)

class Stage(models.Model):
    STAGE_CHOICE = [
        ('ORC', 'Orçamento e aprovação'),
        ('COR', 'Corte de materiais'),
        ('LIX', 'Lixamento e preparação'), 
        ('MON', 'Montagem estrutural'),
        ('PNT', 'Acabamento e pintura'),
        ('SEC', 'Secagem e ajustes finais'),
        ('REV', 'Revisão e controle de qualidade'),
        ('ENT', 'Pronto para retirada/entrega')
    ]

    stage = models.CharField(max_length=3, choices=STAGE_CHOICE, default='ORC')
    order_number = models.ForeignKey(Order, on_delete=models.CASCADE, blank=False, null=False)
    pictures = models.ImageField(upload_to=upload_path, null=True, blank=True)

    def get_stage(self):
        return dict(self.STAGE_CHOICE).get(self.stage, 'Desconhecido')
    