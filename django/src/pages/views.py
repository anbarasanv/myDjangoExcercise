from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request,"index.html",{})

def about_view(request, *args, **kwargs):
    page_conntent = {
        'title':"This is about me!",
        'index':[1,2,3,4,5]
    }
    return render(request,"about.html",page_conntent)

def contact_view(request, *args, **kwargs):
    return render(request,"contact.html",{})