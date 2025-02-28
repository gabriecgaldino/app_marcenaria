from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_orders_view, name='orders'),
    path('new-order/', views.create_order_view, name='new-order'),
    path('remove/<str:order_number>/', views.delete_order_view, name='remove_order'),
    path('<str:order_number>/', views.edit_order_view, name='edit_order')
]