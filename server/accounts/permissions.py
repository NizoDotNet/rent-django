from rest_framework.permissions import BasePermission

class LandlordPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'landlord'