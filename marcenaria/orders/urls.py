from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_order_view, name='orders'),
    path('remove/<str:order_number>/', views.delete_order_view, name='remove_order')
]