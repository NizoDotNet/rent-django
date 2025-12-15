from rest_framework import serializers
from ..models import Listing
from accounts.serializers.OwnerSerializer import OwnerSerializer

class ListingSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)
    class Meta:
        model = Listing
        fields = ('id', 'title', 'description', 'city', 'price_per_night', 'max_guests', 'created_at', 'owner')