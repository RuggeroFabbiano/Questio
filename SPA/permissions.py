"""
Permissions for SPA app.
"""

from rest_framework import permissions

class ReadOnlyOrIsAuthor(permissions.BasePermission):
    """
    Grants permission for reading or if user is author
    """
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or obj.author==request.user
