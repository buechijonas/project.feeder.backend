from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from rest_framework.permissions import BasePermission


def create_verify_permission_and_group():
    # create verify_user permission
    permission, created = Permission.objects.get_or_create(
        codename="verify_user",
        name="Can verify user",
        content_type__app_label="auth",
    )

    # create verified group, if not exists
    group, created = Group.objects.get_or_create(name="verified")

    # add the permission to the verified group
    group.permissions.add(permission)


def create_assignmod_permission_and_group():
    # create assign_moderator permission
    permission, created = Permission.objects.get_or_create(
        codename="assign_moderator",
        name="Can assign moderator",
        content_type__app_label="auth",
    )

    # create moderator group, if not exists
    group, created = Group.objects.get_or_create(name="moderator")

    # add the permission to the moderator group
    group.permissions.add(permission)


class CanViewUserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('authentication.view_user')

class CanAddUserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('authentication.add_user')

class CanChangeUserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('authentication.change_user')

class CanDeleteUserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('authentication.delete_user')