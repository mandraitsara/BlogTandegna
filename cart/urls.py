from django.urls import path
from cart.views import cart
from . import views

urlpatterns = [
    path('', cart, name="cart"),
]
