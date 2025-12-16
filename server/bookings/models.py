from django.db import models
from accounts.models import User
from listings.models import Listing
from django.core.exceptions import ValidationError

class BookingRequest(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
        ('cancelled', 'Cancelled')
    )

    id = models.AutoField()
    check_in = models.DateField(auto_now=False, auto_now_add=False)
    check_out = models.DateField(auto_now=False, auto_now_add=False)
    guests = models.PositiveSmallIntegerField()
    nights = models.PositiveIntegerField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICE,
        default='pending'
    )

    total_price = models.DecimalField(max_digits=6, decimal_places=2, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name='listing'
    )

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user'
    )

    def clean(self):
        if self.check_out <= self.check_in:
            raise ValidationError("Check-out must be after check-in")

        if self.guests > self.listing.max_guests:
            raise ValidationError("Guest count exceeds listing capacity")

    def save(self, *args, **kwargs):
        self.nights = (self.check_out - self.check_in).days
        self.total_price = self.nights * self.listing.price_per_night
        super().save(*args, **kwargs)

