from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('d1', views.demo1, name="demo1"),
    path('d2', views.demo2, name="demo2"),
]