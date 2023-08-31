from rest_framework import serializers

from leave.models import LeaveRequest, LeaveType
from users.models import Users

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType
        fields = ['id', 'name', 'days', 'description',]

class LeaveRequestSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='Users.name')
    leave_type_name = serializers.ReadOnlyField(source='LeaveType.name')

    class Meta:
        model = LeaveRequest
        fields = ['id', 'employee', 'employee_name', 'leave_category', 'leave_category_name', 'start_date', 'end_date', 'reason', 'status', 'created_at', 'updated_at']