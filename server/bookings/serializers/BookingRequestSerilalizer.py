from rest_framework import serializers
from ..models import BookingRequest

class BookingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingRequest
        fields = ('listing', 'check_in', 'check_out', 'guests')

    def validate(self, attrs):
        check_in = attrs.get('check_in')
        check_out = attrs.get('check_out')
        listing = attrs.get('listing')
        guests = attrs.get('guests')

        if check_in and check_out and check_out <= check_in:
            raise serializers.ValidationError({
                "check_out": "Check-out must be after check-in"
            })

        if listing and guests and guests > listing.max_guests:
            raise serializers.ValidationError({
                "guests": "Guest count exceeds listing capacity"
            })

        return attrs
    
    def create(self, validated_data):
        user = self.context['request'].user
        check_in = validated_data['check_in']
        check_out = validated_data['check_out']
        listing = validated_data['listing']

        if BookingRequest.objects.filter(
            listing=listing,
            check_in__lt=check_out,
            check_out__gt=check_in,
            status__in='approved'
        ).exists():
            raise serializers.ValidationError(
                "Listing is already booked for these dates"
            )


        return BookingRequest.objects.create(customer=user, **validated_data)