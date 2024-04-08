from .models import Product,  Order, Category
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

"""
Loads the product page of the website
"""


def index(request):
    cartDict = request.session.get('cart')
    if not cartDict:
        request.session['cart'] = {}
    all_categories = Category.objects.all()
    cat_id = request.GET.get('categorie')
    if cat_id:
        if cat_id == "10":
            products = Product.objects.all()
        else:
            products = Product.fetch_products_by_category(cat_id)
    else:
        products = Product.objects.all()
    all_data = {}
    all_data['products'] = products
    all_data['categories'] = all_categories
    product_id = request.POST.get('product')
    is_remove = request.POST.get('remove')
    if product_id is not None:
        cartDict = request.session.get('cart')
        if cartDict:
            quantity = cartDict.get(product_id)
            if quantity:
                if is_remove:
                    if quantity <= 1:
                        cartDict.pop(product_id)
                    else:
                        cartDict[product_id] = quantity - 1
                else:
                    cartDict[product_id] = quantity + 1
            else:
                cartDict[product_id] = 1
        else:
            cartDict = {}
            cartDict[product_id] = 1
        request.session['cart'] = cartDict
        total_price = 0
        if request.session['cart']:
            for id in request.session['cart']:
                qty = request.session['cart'][id]
                p = Product.objects.get(id=id)
                total_price += p.price * qty
        request.session['final_price'] = total_price
    return render(request, 'index.html', all_data)