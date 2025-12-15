from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers.ListListingSerializer import ListListingSerializer
from .serializers.CreateListingSerializer import CreateListingSerializer
from .serializers.ListingSerializer import ListingSerializer
from rent.permissions import IsLandlordPermission 
from .models import Listing


class CreateListListingsView(ListCreateAPIView):
    queryset = Listing.objects.all().order_by('-created_at')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListListingSerializer
        return CreateListingSerializer
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsLandlordPermission()]
        return []
    
class RetrieveUpdateDestroyListingView(RetrieveUpdateDestroyAPIView):
    serializer_class = ListingSerializer
    lookup_field = 'id'
    queryset = Listing.objects.select_related('owner')


    