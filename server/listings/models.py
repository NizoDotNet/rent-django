from django.db import models
from accounts.models import User 
from django.core.validators import MinValueValidator, MinLengthValidator
class Listing(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=20, validators=[MinLengthValidator(2)])
    description = models.CharField(max_length=200,  validators=[MinLengthValidator(2)])
    city = models.CharField(max_length=15, validators=[MinLengthValidator(2)])
    price_per_night = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    max_guests = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='owner'
    )
