from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request, *args, **kwargs):
    return HttpResponse('<h1>Welcome to the club, body</h1>')

