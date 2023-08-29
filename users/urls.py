from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserAPIView.as_view()),
    path('getusers/', views.GetUserAPIView.as_view()),
]