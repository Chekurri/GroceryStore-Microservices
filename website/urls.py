from django.urls import path

from . import PaymentPage
from .ConfirmationPage import confirm
from . import CartPage
from . import ProductPage
from . import SummaryPage
from . import ShippingPage
urlpatterns = [
    path('', ProductPage.index),
    path('cart/', CartPage.cart,name='index'),
    path('shipping/', ShippingPage.shipping ),
    path('payment/', PaymentPage.payment, name="payment"),
    path('summary/', SummaryPage.summary, name ="summary"),
    path('confirm/', confirm, name='confirm'),
]