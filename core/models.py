from django.db import models
from django.contrib.auth.models import User

class SourceChoices(models.TextChoices):
    WEBSITE = 'website', 'Website'
    EMAIL = 'email', 'E-mail'
    PHONE = 'phone', 'Telefone'
    OTHER = 'other', 'Outro'

class StatusChoices(models.TextChoices):
    PENDING = 'pending', 'Pendente'
    APPROVED = 'approved', 'Aprovado'
    REJECTED = 'rejected', 'Rejeitado'

class AcessRequest(models.Model):
    user_request = models.ForeignKey(User, on_delete=models.CASCADE)

    source = models.CharField(
        max_length=20,
        choices=SourceChoices.choices,
        default=SourceChoices.WEBSITE
    )

    reason = models.TextField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )

    date_request = models.DateField(auto_now_add=True)

    date_approved = models.DateField(null=True, blank=True)

    admin_approved = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='approved_requests'
    )

class AuditLog(models.Model):
    action = models.CharField(max_length=20,choices=StatusChoices.choices)
    user_action = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    target = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True)

