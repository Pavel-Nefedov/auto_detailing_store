from django.urls import path

import orders.views as ordersapp

app_name = 'orders'

urlpatterns = [
    path('', ordersapp.OrderList.as_view(), name='index'),
    path('forming/complete/<int:pk>/', ordersapp.order_forming_complete, name='order_forming_complete'),
    path('create/', ordersapp.OrderCreate.as_view(), name='order_create'),
    path('read/<int:pk>/', ordersapp.OrderRead.as_view(), name='order_read'),
    path('update/<int:pk>/', ordersapp.OrderUpdate.as_view(), name='order_update'),
    path('delete/<int:pk>/', ordersapp.OrderDelete.as_view(), name='order_delete'),
    path('product/<int:pk>/price/', ordersapp.get_product_price)
]