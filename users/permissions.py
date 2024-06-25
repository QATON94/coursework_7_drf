from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверяет, является ли пользователь владельцем"""

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False


class SignPublicity(BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.sign_publicity:
            return True
        return False
