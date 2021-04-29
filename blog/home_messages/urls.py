from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('blogs/', views.home_messages, name = "home_messages"),


]