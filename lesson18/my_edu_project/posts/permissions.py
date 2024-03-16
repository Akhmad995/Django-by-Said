from rest_framework import permissions
    

class iAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        return bool(request.method in permissions.SAFE_METHODS or request.user.is_authenticated)
    
    def has_object_permission(self, request, view, obj) -> bool:
        return bool(obj.author == request.user)