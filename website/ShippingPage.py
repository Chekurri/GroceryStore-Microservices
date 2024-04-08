
from django.shortcuts import render, redirect
from django.contrib import messages

""" This function loads the shipping page"""


def shipping(request):
    # Check if the cart exists and has at least one product
    cart = request.session.get('cart', {})
    if cart and any(quantity > 0 for quantity in cart.values()):
        return render(request, 'shipping.html')
    else:
        # Optional: Add a message to inform the user
        messages.info(request, "Your cart is empty. Please add products before proceeding to shipping.")
        return redirect('index')  # Replace 'index' with the name of your view that shows the products

