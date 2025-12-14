from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, OpenApiResponse
from ..serializers.RegisterSerializer import RegisterSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]
    @extend_schema(
            summary="User registration",
            request=RegisterSerializer,
            responses={
                201: OpenApiResponse(
                    description="User registered successfully"
                ),
                400: OpenApiResponse(
                    description="Validation error"
                ),
            },
            tags=["Authentication"],
        )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
