from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Users

from users.serializers import UserSerializer


class UserAPIView(APIView):
    def post(self, request):
        name = request.data.get('name')
        gender = request.data.get('gender')
        department = request.data.get('department')
        phone_number = request.data.get('phone_number')
        email_address = request.data.get('email_address')

        users = Users.objects.create(
            name = name,
            gender = gender,
            department = department,
            phone_number = phone_number,
            email_address = email_address
        )
        return Response({
            "status":True,
            "name":name,
            "gender":gender,
            "department":department,
            "phone_number":phone_number,
            "email_address":email_address
        })

class GetUserAPIView(APIView):
    def get(self,request):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({
            "status":True,
            "name":serializer.data
        })