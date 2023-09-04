from rest_framework import serializers

from leave.models import LeaveType
from users.models import Users

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'username', '' 'gender', 'department', 'phone_number', 'email_address', 'password']