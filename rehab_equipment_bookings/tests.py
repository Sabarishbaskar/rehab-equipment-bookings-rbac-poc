from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserRole


class TestRBACRoles(TestCase):

    def setUp(self):

        self.admin_user = User.objects.create_user(
            username="admin_user",
            password="test123"
        )

        self.staff_user = User.objects.create_user(
            username="staff_user",
            password="test123"
        )

        self.viewer_user = User.objects.create_user(
            username="viewer_user",
            password="test123"
        )

        UserRole.objects.create(
            user=self.admin_user,
            role="admin"
        )

        UserRole.objects.create(
            user=self.staff_user,
            role="assigned_staff"
        )

        UserRole.objects.create(
            user=self.viewer_user,
            role="viewer"
        )

    def test_admin_role(self):
        self.assertEqual(
            self.admin_user.userrole.role,
            "admin"
        )

    def test_staff_role(self):
        self.assertEqual(
            self.staff_user.userrole.role,
            "assigned_staff"
        )

    def test_viewer_role(self):
        self.assertEqual(
            self.viewer_user.userrole.role,
            "viewer"
        )

# Create your tests here.
