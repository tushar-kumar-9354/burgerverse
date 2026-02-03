from django.urls import path
from .views import add_to_cart, remove_from_cart, cart_detail, checkout, order_success

app_name = 'orders'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('success/', order_success, name='order_success'),
]
