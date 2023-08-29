from rest_framework import serializers

from leave.models import LeaveType

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType
        fields = ['name', 'days', 'description',]