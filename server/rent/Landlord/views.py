from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

class LandlordViewSet(ViewSet):
    def list(self, request):
        return Response({"message": "Landlord service is running"})

   
    @action(detail=False, methods=['get'])
    def health(self, request):
        return Response({"status": "OK"})
