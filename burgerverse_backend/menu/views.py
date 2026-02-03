from django.shortcuts import render
from .models import Category

def menu_list(request):
    """
    Displays all active categories with available products.
    """

    categories = Category.objects.filter(is_active=True).prefetch_related(
        'products'
    )

    return render(request, 'menu/menu_list.html', {
        'categories': categories
    })
