from rest_framework import permissions


class IsAuthorOfPost(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, article):
        if request.user:
            return request.user == article.author
        return False
