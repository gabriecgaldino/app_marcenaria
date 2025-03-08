from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.list_orders_view, name='orders'),
    path('new-order/', views.create_order_view, name='new-order'),
    path('remove/<str:order_number>/', views.delete_order_view, name='remove_order'),
    path('<str:order_number>/', views.edit_order_view, name='edit_order'),
    path('<str:order_number>/<int:stage_id>/', views.add_stage_photo, name='update_stage')
]