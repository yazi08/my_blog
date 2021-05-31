from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views.generic import DetailView,CreateView,ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.views import *





class HomeDetailView(DetailView):
    model = Blog
    template_name = "home_detail.html"
    context_object_name = 'blog'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu']=menu
        return context

    # def get_queryset(self):
    #
    #     return Blog.objects.filter(cat__slug=self.kwargs['slug'])

# def homedeta(request,pk):
#     blog = Blog.objects.filter(pk=pk)
#     context ={
#         'blog':blog
#
#     }
#     return render(request, 'home_detail.html', context=context)

class HomeMessages(ListView):
    paginate_by = 1
    model = Blog
    template_name = "home_messages.html"
    context_object_name = 'data'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu']=menu
        return context
#
#

# def homemess(request):
#     data = Blog.objects.all()
#     context_1 = {
#         'paginate_by' : 1,
#         'data' :data,
#
#
#     }
#     return render(request, 'home_messages.html', context_1=context_1)

#
class ShowCategory(ListView):
    model = Blog
    template_name = 'category_1.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu']=menu
        return context
    def get_queryset(self):

         return Blog.objects.filter(cat__slug=self.kwargs['cat_slug'])


# def show_category(request,cat_id):
#     posts = Blog.objects.filter(pk=cat_id)
#     cats = Category.objects.all()
#     context = {
#         'posts':posts,
#         'menu': menu,
#
#     }
#     return render(request, 'category_1.html', context=context)


def show_category_1(request):
    cats = Category.objects.all()
    context = {

        'cats':cats,
        'menu': menu,

    }
    return render(request,'category.html', context=context)


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_1 = super().get_context_data(**kwargs)
        context_1['menu'] = menu
        context = super().get_context_data(**kwargs)
        return context_1
