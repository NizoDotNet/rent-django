from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.status as status
from ..permissions import LandlordPermission

class GetRoleView(APIView):
    permission_classes = [LandlordPermission]
    def get(self, request):
        return Response({ 'role': request.user.role }, status=status.HTTP_200_OK)