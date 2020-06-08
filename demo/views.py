from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def demo1(request):
    return HttpResponse("Demo 1 to present")

def demo2(request):
    return HttpResponse("Demo 2 to present")