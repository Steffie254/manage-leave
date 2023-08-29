from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('leaves/', views.LeaveTypesAPIView.as_view()),
    path('getleaves/', views.GetLeaveTypes.as_view()),
]