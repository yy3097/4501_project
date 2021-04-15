from django.shortcuts import render

def home(request):
    return render(request,'tracker/home.html',{})

# Create your views here.
