from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers.ListListingSerializer import ListListingSerializer
from .serializers.CreateListingSerializer import CreateListingSerializer
from rent.permissions import IsLandlordPermission 

from .models import Listing


class ListListingsView(ListAPIView):
    serializer_class = ListListingSerializer
    queryset = Listing.objects.all()

    
class CreateListingView(CreateAPIView):
    # permission_classes = [IsLandlordPermission]
    queryset = Listing.objects.all()
    serializer_class = CreateListingSerializer