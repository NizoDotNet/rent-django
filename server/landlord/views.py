from django.shortcuts import render

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, OpenApiExample

class LandlordViewSet(ViewSet):

    @extend_schema(
        summary="List landlords (health check)",
        description="Simple endpoint to verify the landlord service is running",
        responses={200: dict}
    )
    def list(self, request):
        return Response({"message": "Landlord service is running"})

    @extend_schema(
        summary="Create landlord",
        description="Creates a landlord using name and email",
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "email": {"type": "string"}
                },
                "required": ["name", "email"]
            }
        },
        responses={201: dict},
        examples=[
            OpenApiExample(
                "Create landlord example",
                value={"name": "John Doe", "email": "john@mail.com"}
            )
        ]
    )
    def create(self, request):
        name = request.data.get("name")
        email = request.data.get("email")

        return Response({
            "name": name,
            "email": email,
            "message": "Landlord created successfully"
        })

    @extend_schema(
        summary="Health check",
        description="Dedicated health endpoint",
        responses={200: dict}
    )
    @action(detail=False, methods=['get'])
    def health(self, request):
        return Response({"status": "OK"})
