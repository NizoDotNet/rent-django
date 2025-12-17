from django.db import models
import uuid
from bookings.models import BookingRequest

class Checkout(models.Model):
    STATUS_CHOICE = (
        ('initiated', 'Initiated'),
        ('paid', 'Paid'),
        ('failed', 'Failed')
    )
    id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(
        BookingRequest,
        on_delete=models.SET_NULL,
        related_name='checkout'
    )
    amount = models.DecimalField(max_digits=6, decimal_places=2, editable=False)
    status = status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICE,
        default='initiated'
    )

    created_at = models.DateTimeField(auto_now_add=True, editable=False)

class Payment(models.Model):
    STATUS_CHOICE = (
        ('success', 'Success'),
        ('failed', 'Failed')
    )
    id = models.AutoField(primary_key=True)
    checkout = models.ForeignKey(
        Checkout,
        on_delete=models.CASCADE,
        related_name='payment'
    )
    provider = models.CharField(max_length=10)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, editable=False)
    transaction_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)


