from rest_framework.generics import CreateAPIView
from rent.permissions import IsCustomerPermission
from .models import BookingRequest
from .serializers.BookingRequestSerilalizer import BookingRequestSerializer

class BookingView(CreateAPIView):
    permission_classes = [IsCustomerPermission]
    serializer_class = BookingRequestSerializer
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

