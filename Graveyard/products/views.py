from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer

from random import randint

from .models import Product

def helloworld(request):
    template = get_template('one.html')
    response_body = template.render({}, request)
    response_body = response_body.replace('cat', 'dog')
    return HttpResponse(response_body)

    return render(request, 'one.html', {})

def home(request):
    return render(request, 'home.html', {})


@login_required
@permission_required('is_superuser')
def alireza(request):
    products = [
        "Foo", "Bar", "Goo", "Apple", 
    ]

    context = {"qty": randint(1000,9999),
               "products": products}
    return render(request, 'lezzat.html', context)


def form1(request, errno=0):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if password != "ost":
            return redirect('form1', errno=2)
        # return HttpResponse(f"{username}:{password}")
        return redirect('home')

    elif request.method == 'GET':
        context = {"errno": errno}
        return render(request, 'form1.html', context)
    
def list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'list.html', context)

def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {"product": product}
    return render(request, 'detail.html', context)

def delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('list')

    
@api_view(["GET"])
def testdrf(request):    
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


