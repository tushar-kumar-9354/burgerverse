from decimal import Decimal
from .models import Order, OrderItem
from menu.models import Product

def create_cart_for_user(user):
    """
    Creates a new cart (Order) for a user.
    """
    return Order.objects.create(user=user)


def add_product_to_cart(order, product_id, quantity=1):
    """
    Adds a product to the cart or updates quantity.
    """

    product = Product.objects.get(id=product_id)

    order_item, created = OrderItem.objects.get_or_create(
        order=order,
        product=product,
        defaults={'price': product.price}
    )

    if not created:
        order_item.quantity += quantity
    else:
        order_item.quantity = quantity

    order_item.save()
    recalculate_order_total(order)


def remove_product_from_cart(order, product_id):
    """
    Removes a product from the cart.
    """
    OrderItem.objects.filter(
        order=order,
        product_id=product_id
    ).delete()

    recalculate_order_total(order)


def recalculate_order_total(order):
    """
    Recalculates total price of an order.
    """

    total = Decimal('0.00')

    for item in order.items.all():
        total += item.price * item.quantity

    order.total_price = total
    order.save()

def checkout_order(order):
    """
    Finalizes the order and locks it.
    """
    if order.items.count() == 0:
        raise ValueError("Cannot checkout an empty cart")

    order.status = 'PREPARING'
    order.save()
