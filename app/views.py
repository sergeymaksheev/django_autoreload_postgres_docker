from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def status(request):
    return HttpResponse("<h1>Status OK</h1>")