from .models import *
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def landing_page(request):
    return HttpResponse("annyeong ini nuri")

def second_page(request):
    return HttpResponse("SecondPage")

def profile(request):
    return HttpResponse('My Profile')

def count(request, angka):
    angka = angka+1
    return HttpResponse(str(angka))

def sapa(request, nama):
    return HttpResponse("halo "+nama)

def example(request):
    return render(request, 'example.html')

def shop(request):
    return render(request, 'shop.html')

def home(request):
    return render(request, 'home.html')

def list_produk_decoration(request):
    try:
        print(request.GET)
        category_decoration = Category.objects.get(pk=1)
        #pk == primary_key
        if(request.GET=={}):
            product_decoration = Product.objects.filter(category=category_decoration)
        else:
            product_decoration = Product.objects.filter(category=category_decoration).filter(
                name__icontains=request.GET['product_name'])

        # WHERE name like 'chrome'
        if(product_decoration.count() != 0):
            return render(request, 'list_produk_decoration.html', {'product_list': product_decoration, 'available': True})
        else:
            return render(request, 'list_produk_decoration.html', {'available': False})
    except:
        return HttpResponse("Terjadi Error")