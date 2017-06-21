from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, World. You are at the pools index.")


def salut(request):
    return HttpResponse("Hello you are in the salut view.")

# Create your views here.
