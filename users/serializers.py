from rest_framework import serializers

from leave.models import LeaveType
from users.models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'gender', 'department', 'phone_number', 'email_address']