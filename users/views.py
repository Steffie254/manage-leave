from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Users

from users.serializers import UserSerializer


class UserAPIView(APIView):
    def post(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        gender = request.data.get('gender')
        department = request.data.get('department')
        phone_number = request.data.get('phone_number')
        email_address = request.data.get('email_address')

        users = Users.objects.create(
            first_name = first_name,
            last_name = last_name,
            gender = gender,
            department = department,
            phone_number = phone_number,
            email_address = email_address,
        )
        return Response({
            "status":True,
            "first_name":first_name,
            "last_name":last_name,
            "gender":gender,
            "department":department,
            "phone_number":phone_number,
            "email_address":email_address,
        })

class GetUserAPIView(APIView):
    def get(self,request):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({
            "status":True,
            "name":serializer.data
        })