from django.shortcuts import render
from inventory.models import User

# Create your views here.

def index(request):
    return render(request,'index.html')

def wish(request):
    return render(request,'wish.html')