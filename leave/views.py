from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from leave.models import LeaveRequest, LeaveType

from leave.serializers import LeaveRequestSerializer, LeaveSerializer


class LeaveTypesAPIView(APIView):
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
    

class LeaveRequestAPIView(APIView):
    def post(self, request):
        employee = request.data.get('employee')
        leave_type = request.data.get('leave_type')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        reason = request.data.get('reason')
        status = request.data.get('status')
        created_at = request.data.get('created_at')
        updated_at = request.data.get('update_at')

        leave_requests = LeaveRequest.objects.create(
            employee = employee,
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
        