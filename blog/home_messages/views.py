from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from django.views.generic import  DetailView



class HomeDetailView(DetailView):
    model = Blog
    template_name = "home_detail.html"
    context_object_name = 'blog'


def home_messages(request):
    data = Blog.objects.all()
    return render(request, "home_messages.html", {'data':data})