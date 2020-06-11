from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Team, Portfolio, Blog

def index(request):
    teams = Team.objects.all()
    portfolios = Portfolio.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'demo/index.html', {'teams': teams,
    'portfolios': portfolios,
    'blogs': blogs,
    })