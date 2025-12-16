from rest_framework import serializers
from core.models import AcessRequest, AuditLog
from django.contrib.auth.models import User
class AcessRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcessRequest
        fields = [
            'id',
            'user_request',
            'source',
            'reason',
            'status',
            'date_request',
            'date_approved',
            'admin_approved'
        ]
class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = [
            'id',
            'action',
            'user_action',
            'target',
            'timestamp',
            'details'
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff',
            'is_active',
            'date_joined'
        ]
