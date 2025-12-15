from rest_framework.permissions import BasePermission

class LandlordPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'landlord'
    

class CustomerPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'customer'