from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from leave.models import LeaveType

from leave.serializers import LeaveSerializer


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