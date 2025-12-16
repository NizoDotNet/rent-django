from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .serializers import BookingRequestSerializer, GetBookingRequestSerializer, ResultSerializer
from rest_framework.permissions import IsAuthenticated
from .models import BookingRequest
from rent.permissions import IsLandlordPermission
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_201_CREATED
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
from drf_spectacular.types import OpenApiTypes

class BookingView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BookingRequest.objects.all()

    def get_queryset(self):
        user = self.request.user

        if user.role == 'customer':
            return BookingRequest.objects.filter(customer=user)

        if user.role == 'landlord':
            return BookingRequest.objects.filter(listing__owner=user)

        return BookingRequest.objects.none()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetBookingRequestSerializer
        return BookingRequestSerializer
    
    
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
    

class BookingChangeStatusView(APIView):
    permission_classes = [IsLandlordPermission]

    def __init__(self, status, **kwargs):
        self.status = status
        super().__init__(**kwargs)
    @extend_schema(
        description="Approve a booking by ID (only the listing owner can approve)",
        parameters=[
            OpenApiParameter(
                name='id',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
                description="ID of the booking to approve"
            ),
        ],
        responses={
            201: OpenApiResponse(
                response=ResultSerializer,
                description="Booking updated successfully"
            ),
            404: OpenApiResponse(
                response=ResultSerializer,
                description="Booking not found or user is not the owner"
            ),
            500: OpenApiResponse(
                response=ResultSerializer,
                description="Internal server error"
            ),
        }
    )
    def post(self, request, id):
        try:
            booking = BookingRequest.objects.get(id=id)
            if booking.listing.owner != request.user:
                return Response(status=HTTP_404_NOT_FOUND, data={ 'result': 'No such booking with this id'} )

            booking.status = self.status
            booking.save()
        except BookingRequest.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND, data={ 'result': 'No such booking with this id'} )
        except Exception as ex:
            raise ex 
        return Response(status=HTTP_201_CREATED, data={'result': 'Updated succesfully'})
        

class BookingApproveView(BookingChangeStatusView):
    def __init__(self, **kwargs):
        super().__init__('approved', **kwargs)

class BookingRejectView(BookingChangeStatusView):
    def __init__(self, **kwargs):
        super().__init__('rejected', **kwargs)
