from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Blog
from django.views.generic import DetailView,CreateView,ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class HomeDetailView(DetailView):
    model = Blog
    template_name = "home_detail.html"
    context_object_name = 'blog'

class HomeMessages(ListView):
    paginate_by = 1
    model = Blog
    template_name = "home_messages.html"
    context_object_name = 'data'






class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))
