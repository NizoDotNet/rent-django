from django.db import models
from accounts.models import User 

class Listing(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    city = models.CharField(max_length=15)
    price_per_night = models.DecimalField(max_digits=5, decimal_places=2)
    max_guests = models.IntegerField()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='owner'
    )
