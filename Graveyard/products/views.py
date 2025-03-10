from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from random import randint

def helloworld(request):
    template = get_template('one.html')
    response_body = template.render({}, request)
    response_body = response_body.replace('cat', 'dog')
    return HttpResponse(response_body)

    return render(request, 'one.html', {})

def home(request):
    return render(request, 'home.html', {})


def alireza(request):
    products = [
        "Foo", "Bar", "Goo", "Apple", 
    ]

    context = {"qty": randint(1000,9999),
               "products": products}
    return render(request, 'lezzat.html', context)

def list(request):
    context = {"err": "test1"}
    return JsonResponse(context)
