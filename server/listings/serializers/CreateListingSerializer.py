from rest_framework import serializers
from ..models import Listing

class CreateListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('title', 'description', 'city', 'price_per_night', 'max_guests')
    def create(self, validated_data):
        user = self.context['request'].user
        return Listing.objects.create(owner=user, **validated_data)