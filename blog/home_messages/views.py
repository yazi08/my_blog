from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

def home_messages(request):
    data = Blog.objects.all()
    return render(request, "home_messages.html", {'data':data})