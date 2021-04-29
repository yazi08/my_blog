from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home_messages, name = "home_messages"),
    path('<int:pk>', views.HomeDetailView.as_view(), name = 'home_detail')

]