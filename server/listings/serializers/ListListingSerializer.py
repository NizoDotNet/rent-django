from rest_framework import serializers
from ..models import Listing
class ListListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('id', 'title', 'description', 'city', 'price_per_night', 'max_guests')