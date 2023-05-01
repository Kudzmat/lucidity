from django.contrib import admin
from django.urls import path, include
from orders import views

app_name = "orders"

urlpatterns = [
    path("", views.orders_reg, name='orders'),
    path("local-orders/", views.new_local, name='local'),
    path("sa-orders/", views.new_sa, name='sa'),
    path("complete-order/", views.complete_order, name='complete')
]
