from django.shortcuts import render,HttpResponse
# Create your views here.


def main(request):
    return HttpResponse("Hello from main view")


def index(request):
    return HttpResponse("Hello from index view")