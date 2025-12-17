from rest_framework.views import APIView
from bookings.models import BookingRequest
from rent.permissions import IsCustomerPermission
from rest_framework.response import Response
from .models import Checkout, Payment
from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiResponse,
)
class CheckoutBookingView(APIView):
    permission_classes = [IsCustomerPermission]
    def post(self, request, booking_id):
            
        try:
            booking = BookingRequest.objects.filter(
                customer=request.user,
                status='approved'
            ).get(id=booking_id)

        except BookingRequest.DoesNotExist:
            return Response(status=404)
        
        Checkout.objects.create(
            booking=booking,
            amount=booking.total_price
        )

        return Response(status=201)
    
class PayView(APIView):
    permission_classes = [IsCustomerPermission]
    @extend_schema(
        summary="Confirm checkout payment",
        description=(
            "Confirms payment for an approved booking request. "
            "Creates a payment record and updates checkout status "
            "based on the `success` query parameter."
        ),
        parameters=[
            OpenApiParameter(
                name="id",
                description="Checkout ID",
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            ),
            OpenApiParameter(
                name="success",
                description="Payment result. `true` for successful payment, `false` otherwise.",
                required=True,
                type=bool,
                location=OpenApiParameter.QUERY,
            ),
        ],
        responses={
            201: OpenApiResponse(
                response=None,
                description="Payment processed successfully"
            ),
            400: OpenApiResponse(
                response=None,
                description='Something went wrong while payment'
            ),
            404: OpenApiResponse(
                response=None,
                description="Checkout not found or not approved"
            ),
        },
    )
    def post(self, request, id):
        checkout = None
        try:
            checkout = Checkout.objects.filter(
                booking__customer=request.user,
                status='initiated'
            ).get(id=id)

        except Checkout.DoesNotExist:
            return Response(status=404)
        
        success = request.query_params.get('success')
        print(success)
        if success:
            Payment.objects.create(
                checkout=checkout,
                provider='Fake',
                status='success'
            )
            checkout.status = 'paid'
            checkout.save()
            return Response(status=201)

        else:
            Payment.objects.create(
                checkout=checkout,
                provider='Fake',
                status='failed'
            )
            checkout.status = 'failed'
            checkout.save()
            return Response(status=400)


