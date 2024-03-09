from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome to my e_commerce home page")

def gallery(request):
    return HttpResponse("You can view a sample of the goods we sell")
