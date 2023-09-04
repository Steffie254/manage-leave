from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('leaves/', views.LeaveTypesAPIView.as_view()),
    path('getleaves/', views.GetLeaveTypes.as_view()),
    path('leaverequests/', views.LeaveRequestAPIView.as_view()),
    path('userleaves/', views.UserLeavesAPIView.as_view())
]
