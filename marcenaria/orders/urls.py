from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_order_view, name='orders'),
]