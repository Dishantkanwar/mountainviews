import http
from django.shortcuts import render
from django.shortcuts import HttpResponse
from.models import *

def home(request):
    return render(request,'home.html')

# Create your views here.
