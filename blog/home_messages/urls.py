from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.HomeMessages.as_view(), name = "home_messages"),
    path('<int:pk>', views.HomeDetailView.as_view(), name = 'home_detail'),
    path('register/', views.RegisterUser.as_view(), name = 'register'),
]