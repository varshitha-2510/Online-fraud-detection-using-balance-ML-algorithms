from django.db import models
import uuid

class TransactionVerification(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )

    sender_username = models.CharField(max_length=100)
    sender_email = models.EmailField()
    receiver_email = models.EmailField()

    amount = models.FloatField()
    risk_level = models.CharField(max_length=20)
    risk_score = models.FloatField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    verification_token = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Txn {self.id} | {self.risk_level} | {self.status}"
