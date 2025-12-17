from rest_framework import serializers
from ..models import Listing
from rest_framework.exceptions import ValidationError
class CreateListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('title', 'description', 'city', 'price_per_night', 'max_guests')
    def create(self, validated_data):
        user = self.context['request'].user
        return Listing.objects.create(owner=user, **validated_data)
    
    def validate(self, attrs):
        price = attrs.get('price_per_night')
        max_guests = attrs.get('max_guests')
        title = attrs.get('title')
        description = attrs.get('description')
        city = attrs.get('city')

        if not len(title) >= 2:
            raise ValidationError({
                'title': 'Title must contain at least 2 characters' 
            })
        
        if not len(description) >= 2:
            raise ValidationError({
                'description': 'Description must contain at least 2 characters' 
            })

        if not len(city) >= 2:
            raise ValidationError({
                'city': 'city must contain at least 2 characters' 
            })
        
        if price < 0:
            raise ValidationError({
                'price': 'Price cannot be less than zero' 
            })

        if max_guests <= 0:
            raise ValidationError({
                'guests': 'Guests cannot be less than zero' 
            })