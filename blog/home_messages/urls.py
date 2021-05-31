from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [

    path('blog/', views.HomeMessages.as_view(), name = "home_messages"),
    # path('contact/', views.contact, name = 'contact'),
    # path('pro_nas/', views.pro_nas, name = 'pro_nas'),
    path('blog/<slug:slug>', views.HomeDetailView.as_view(), name = 'blog_key'),
    path('register/', views.RegisterUser.as_view(), name = 'register'),
    path('category/', views.show_category_1, name = 'cat'),
    path('category/<slug:cat_slug>', views.ShowCategory.as_view(), name = 'category'),
]