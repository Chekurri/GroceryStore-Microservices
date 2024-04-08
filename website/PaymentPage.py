
from django.shortcuts import render

""" This function loads the payment page"""
def payment(request):
    request.session['address'] = request.POST.get("address")
    request.session['phone'] = request.POST.get("phone")
    #we add the shipping cost here by default 20
    request.session['delivery_price'] = request.session.get("final_price") + 20
    return render(request, 'payment.html')
