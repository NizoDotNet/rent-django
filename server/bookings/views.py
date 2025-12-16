from rest_framework.views import APIView
from rent.permissions import IsCustomerPermission
from .models import BookingRequest

class IsBookingAvaibleView(APIView):
    permission_classes = [IsCustomerPermission]
    def post(self, request, format=None):
        ...