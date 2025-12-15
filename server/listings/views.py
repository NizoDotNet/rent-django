from rest_framework.generics import ListCreateAPIView
from .serializers.ListListingSerializer import ListListingSerializer
from .serializers.CreateListingSerializer import CreateListingSerializer
from rent.permissions import IsLandlordPermission 

from .models import Listing


class CreateListListingsView(ListCreateAPIView):
    queryset = Listing.objects.all().order_by('-created_at')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListListingSerializer
        return CreateListingSerializer