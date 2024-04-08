from .models import Product,  Order
from django.shortcuts import render
from django.contrib.auth.models import User, auth

""" This function loads the Confirmation page"""

def confirm(request):
    address = request.session.get('address')
    mobile = request.session.get('phone')
    user_id = request.session.get('user_id')
    cart_items = request.session.get('cart')
    product_list = Product.fetch_products(list(cart_items.keys()))
    for prod in product_list:
        order = Order(user=User(id=user_id), product=prod, price=prod.price, quantity=cart_items.get(str(prod.id)), address=address, phone=mobile)
        order.confirm_order()
    request.session['cart'] = {}
    return render(request, 'confirm.html')
