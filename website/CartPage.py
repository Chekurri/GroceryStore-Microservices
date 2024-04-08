"""
This function loads the cart page of the website
"""

from .models import Product
from django.shortcuts import render




def cart(request):
    if request.method == 'POST':
        id_list = list(request.session.get('cart').keys())
        product_list = Product.fetch_products(id_list)
        return render(request, 'cart.html', {'products': product_list })
    else:
        id_list = list(request.session.get('cart').keys())
        product_list = Product.fetch_products(id_list)
        return render(request, 'cart.html', {'products': product_list})

