from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AcessRequest, AuditLog

@receiver(post_save, sender=AcessRequest)
def registrar_log(sender, instance, created, **kwargs):
    if created:
        action = "Criado"
    else:
        action = "Atualizado"

    AuditLog.objects.create(
        action=action,
        user_action=instance.user_request,
        target=f"AcessRequest #{instance.id}",
        details=f"Status atual: {instance.status}"
    )
