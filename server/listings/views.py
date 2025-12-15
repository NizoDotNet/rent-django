from rest_framework.generics import ListAPIView
from .serializers.ListListingSerializer import ListListingSerializer

class ListListingsView(ListAPIView):
    serializer_class = ListListingSerializer