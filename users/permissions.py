from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
    def has_permission(self, request, view, design):
        return bool(request.user and request.user == design.artist)