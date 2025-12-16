from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import AcessRequest, AuditLog
from core.api.serializers import AcessRequestSerializer, AuditLogSerializer, UserSerializer
from django.contrib.auth.models import User



class AcessRequestListCreateView(APIView):
    def get(self, request):
        acess_requests = AcessRequest.objects.all()
        serializer = AcessRequestSerializer(acess_requests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AcessRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        try:
            acess_request = AcessRequest.objects.get(pk=pk)
        except AcessRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AcessRequestSerializer(acess_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            acess_request = AcessRequest.objects.get(pk=pk)
        except AcessRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        acess_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AuditLogListCreateView(APIView):
    def get(self, request):
        audit_logs = AuditLog.objects.all()
        serializer = AuditLogSerializer(audit_logs, many=True)
        return Response(serializer.data)

class UserView(APIView):
    def get(self, request, pk = None):
        if pk is None:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        return Response(serializer.data)
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk = None):
        if pk is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    


