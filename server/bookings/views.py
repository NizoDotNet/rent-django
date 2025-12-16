from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from .serializers import BookingRequestSerializer, GetBookingRequestSerializer
from rest_framework.permissions import IsAuthenticated
from .models import BookingRequest
from rent.permissions import IsLandlordPermission
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND 

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

    def get(self, request):
        id = request.GET.get('id')
        try:
            booking = BookingRequest.objects.filter(owner=request.user).get(id)
            booking.status = self.status
            booking.save()
        except BookingRequest.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND, data={ 'resutlt': 'No such booking with this id'} )
        except Exception as ex:
            raise ex 

