from django.conf import settings
from django.dispatch import receiver
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate

from users.models import Users

from users.serializers import LoginSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken



class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    
    user = Users.objects.get(name='ann')


    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({'access_token': access_token})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserAPIView(APIView):
    def post(self, request):
        name = request.data.get('name')
        gender = request.data.get('gender')
        department = request.data.get('department')
        phone_number = request.data.get('phone_number')
        email_address = request.data.get('email_address')
        password = request.data.get('password')
    

        users = Users.objects.create(
            name = name,
            gender = gender,
            department = department,
            phone_number = phone_number,
            email_address = email_address,
            username = phone_number,
            password = password
        )

        user_password = users.set_password(password)
        
        users.save()
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