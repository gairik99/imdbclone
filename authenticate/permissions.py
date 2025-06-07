from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        # If the request method is safe (GET, HEAD, OPTIONS), allow access
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)

class IsAuthorOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # Allow access if the user is the author of the object
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_name == request.user
           