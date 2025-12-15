from rest_framework.permissions import BasePermission

class IsLandlordPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'landlord'
    
class IsOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        print(obj.owner.id)
        print(request.user.id)
        return obj.owner.id == request.user.id
    
class IsCustomerPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'customer'
    
