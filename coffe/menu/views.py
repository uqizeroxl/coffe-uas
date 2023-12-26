from django.shortcuts import render
from .models import Product


def home (request) :
    return render (request, "home.html")

def menu(request):
    model = Product.objects.all()

    return render(request, "menu.html", {"data" : model})

def keranjang(request):
    return render(request, "keranjang.html")
