from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from home_messages.models import *
from django.views.generic import DetailView,CreateView,ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def home(request):


    return render(request, 'home.html')


