from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [

    path('blog/', views.HomeMessages.as_view(), name = "home_messages"),
    # path('contact/', views.contact, name = 'contact'),
    # path('pro_nas/', views.pro_nas, name = 'pro_nas'),
    path('<int:pk>', views.HomeDetailView.as_view(), name = 'blog_key'),
    path('register/', views.RegisterUser.as_view(), name = 'register'),
    path('category/', views.show_category_1, name = 'cat'),
    path('category/<int:cat_id>', views.show_category, name = 'category'),
]