from rest_framework.permissions import BasePermission


class RBACPermission(BasePermission):

    def has_permission(self, request, view):

        if not hasattr(request.user, 'userrole'):
            return False

        role = request.user.userrole.role

        permissions = {
            "admin": [
                "create",
                "update",
                "cancel",
                "mark_done",
                "list",
                "retrieve"
            ],

            "assigned_staff": [
                "list",
                "retrieve",
                "mark_done"
            ],

            "viewer": [
                "list",
                "retrieve"
            ]
        }

        action = getattr(view, "action_name", None)

        return action in permissions.get(role, [])