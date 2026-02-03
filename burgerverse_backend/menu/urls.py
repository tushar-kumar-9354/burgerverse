from django.urls import path
from .views import menu_list

app_name = 'menu'

urlpatterns = [
    path('', menu_list, name='menu_list'),
]
