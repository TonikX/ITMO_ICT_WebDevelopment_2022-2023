from rest_framework import permissions

from library_app.models import User


class IsLibraryWorker(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role == User.LIBRARY_WORKER
