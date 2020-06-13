from django.shortcuts import render, get_object_or_404
from restaurant.models import *


# Create your views here.


def home_resto(request):
    menus = Menu.objects.all()
    return render(request, 'home_resto.html', {'menus': menus})
    
    
def menus_product(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    return render(request, 'products.html', {'menu': menu})
    
    
def new_product (request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    return render(request, 'new_product.html', {'menu': menu})