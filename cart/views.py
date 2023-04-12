from django.shortcuts import render,redirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView


def cart(request):
    return render(request, 'cart.html')

# Create your views here.


