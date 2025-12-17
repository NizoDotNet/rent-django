from rest_framework.views import APIView
from bookings.models import BookingRequest
from django.shortcuts import get_object_or_404
from rent.permissions import IsCustomerPermission
from rest_framework.response import Response
from .models import Checkout

class CheckoutBookingView(APIView):
    permission_classes = [IsCustomerPermission]
    def post(self, request, booking_id):
            
        booking = get_object_or_404(BookingRequest, id=booking_id)
        
        Checkout.objects.create(
            booking=booking,
            amount=booking.total_price
        )

        return Response(status=201)