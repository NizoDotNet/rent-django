from rest_framework.generics import ListCreateAPIView
from .serializers import BookingRequestSerializer, GetBookingRequestSerializer
from rest_framework.permissions import IsAuthenticated
from .models import BookingRequest
from rent.permissions import IsCustomerPermission

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
    

