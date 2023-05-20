from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def ajit(request):
    return HttpResponse('<h1><marquee>welcome to ghost world</marquee></h1>')