
from decimal import Decimal
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import leave.models 
from leave.models import LeaveRequest, LeaveType, UserLeaves

from leave.serializers import LeaveRequestSerializer, LeaveSerializer, UserLeavesSerializer
from users.models import Users

import json
import time
import uuid
import requests

class LeaveTypesAPIView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request):
        name = request.data.get('name')
        days = request.data.get('days')
        description = request.data.get('description')


        leave_types = LeaveType.objects.create(
            name = name,
            days = days,
            description = description
        )
        return Response({
            "status":True,
            "name":name,
            "days":days,
            "description":description
        })

class GetLeaveTypes(APIView):
    def get(self,request):
        leave_types = LeaveType.objects.all()
        serializer = LeaveSerializer(leave_types, many=True)
        return Response({
            "status":True,
            "name":serializer.data
        })
    
class UserLeavesAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user_id = int(request.data.get('user'))
        user = Users.objects.get(id=user_id)

        leave_id = request.data.get('leave_type')
        leave_type = LeaveType.objects.get(id=leave_id)

        days = leave_type.days
        #days_remaining = request.data.get('days_remaining')


        user_leaves = UserLeaves.objects.create(
            user = user,
            leave_type = leave_type,
            days = days,
            #days_remaining = days
        )
        serializer = UserLeavesSerializer(user_leaves)
        return Response({
            "status":True,
            "name":serializer.data
        })
    

class LeaveRequestAPIView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        user = Users.objects.get(id=user_id)

        leave_id = request.data.get('leave_id')
        leave_type = LeaveType.objects.get(id=leave_id)

        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        reason = request.data.get('reason')
        status = request.data.get('status')
        created_at = request.data.get('created_at')
        updated_at = request.data.get('update_at')
        

        leave_requests = LeaveRequest.objects.create(
            employee = user,
            leave_type = leave_type,
            start_date = start_date,
            end_date = end_date,
            reason = reason,
            status = status,
        
        )

        serializer = LeaveRequestSerializer(leave_requests)
        return Response({
            "status":True,
            "name":serializer.data
        })
        