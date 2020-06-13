from django.shortcuts import render,HttpResponse
from . import models
# Create your views here.


def main(request):
    products = models.Product.objects.all()
    txt=""
    for i in products:
        txt += f"{i.pk},{i.name},{i.price} <Br> "
    return HttpResponse(txt)


def index(request):
    return HttpResponse("Hello from index view")