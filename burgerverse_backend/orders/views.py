from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .services import checkout_order

from .models import Order
from .services import (
    create_cart_for_user,
    add_product_to_cart,
    remove_product_from_cart
)


def get_user_cart(user):
    """
    Returns existing cart or creates a new one.
    """
    cart, created = Order.objects.get_or_create(
        user=user,
        status='PENDING'
    )
    return cart


@login_required
def add_to_cart(request, product_id):
    cart = get_user_cart(request.user)
    add_product_to_cart(cart, product_id)
    return redirect('menu:menu_list')


@login_required
def remove_from_cart(request, product_id):
    cart = get_user_cart(request.user)
    remove_product_from_cart(cart, product_id)
    return redirect('menu:menu_list')

@login_required
def cart_detail(request):
    """
    Displays the current user's cart.
    """
    cart = Order.objects.filter(
        user=request.user,
        status='PENDING'
    ).first()

    return render(request, 'orders/cart_detail.html', {
        'cart': cart
    })

@login_required
def checkout(request):
    """
    Handles checkout and order confirmation.
    """
    cart = Order.objects.filter(
        user=request.user,
        status='PENDING'
    ).first()

    if not cart:
        return redirect('menu:menu_list')

    checkout_order(cart)
    return redirect('orders:order_success')

@login_required
def order_success(request):
    """
    Displays order confirmation.
    """
    return render(request, 'orders/order_success.html')
