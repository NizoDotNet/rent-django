from rest_framework import serializers
from .models import BookingRequest

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

        if listing.owner == user:
            raise serializers.ValidationError(
                "You cannot book your own listing."
            )

        if BookingRequest.objects.filter(
            listing=listing,
            check_in__lt=check_out,
            check_out__gt=check_in,
            status__in=['pending', 'approved'],
        ).exists():
            raise serializers.ValidationError(
                "Listing is already booked for these dates"
            )


        return BookingRequest.objects.create(**validated_data)


class GetBookingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingRequest
        fields = ('id', 'customer', 'listing', 'check_in', 'check_out', 'guests')

    
# class UpdateStatusBookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BookingRequest
#         fields = ['status']
    
#     def validate(self, attrs):
#         status = attrs.get('status')
#         if status not in ('approved', 'rejected'):
#             raise serializers.ValidationError(
#                 "Booking request can only have approved and rejected statuses"
#             )
#         return attrs