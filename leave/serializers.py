from rest_framework import serializers

from leave.models import LeaveRequest, LeaveType, UserLeaves
from users.models import Users

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType
        fields = ['id', 'name', 'days', 'description',]

class UserLeavesSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='Users.name')
    leave_type = serializers.ReadOnlyField(source='LeaveType.name')

    class Meta:
        model = UserLeaves
        fields = ['id', 'user', 'leave_type']

class LeaveRequestSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='Users.name')
    leave_type_name = serializers.ReadOnlyField(source='LeaveType.name')

    class Meta:
        model = LeaveRequest
        fields = ['id', 'user', 'leave_type', 'start_date', 'end_date', 'reason', 'status', 'created_at', 'updated_at']