from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    """
    Custom permission to only allow admin users to access certain views.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff
    

class IsOrganizerUser(BasePermission):
    """
    Custom permission to only allow organizer users to access certain views.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role == 'organizer'


class IsVisitor(BasePermission):
    """
    Custom permission to only allow users with visitor role to access certain views.
    """
    
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'role') and request.user.role == 'visitor'

