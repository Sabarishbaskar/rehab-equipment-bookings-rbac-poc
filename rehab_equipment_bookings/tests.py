from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from .models import (
    UserRole,
    RehabEquipmentBooking
)


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


class TestRBACPermissions(APITestCase):

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

        self.booking = RehabEquipmentBooking.objects.create(
            patient_name="John",
            equipment_name="Wheelchair"
        )

    def test_admin_can_create(self):

        self.client.force_authenticate(
            user=self.admin_user
        )

        response = self.client.post(
            "/api/bookings/",
            {
                "patient_name": "Ram",
                "equipment_name": "Walker"
            },
            format="json"
        )

        self.assertEqual(response.status_code, 201)

    def test_admin_can_update(self):

        self.client.force_authenticate(
            user=self.admin_user
        )

        response = self.client.put(
            f"/api/bookings/{self.booking.id}/",
            {
                "patient_name": "Updated",
                "equipment_name": "Walker"
            },
            format="json"
        )

        self.assertEqual(response.status_code, 200)

    def test_admin_can_cancel(self):

        self.client.force_authenticate(
            user=self.admin_user
        )

        response = self.client.post(
            f"/api/bookings/{self.booking.id}/cancel/"
        )

        self.assertEqual(response.status_code, 200)

    def test_admin_can_mark_done(self):

        self.client.force_authenticate(
            user=self.admin_user
        )

        response = self.client.post(
            f"/api/bookings/{self.booking.id}/mark-done/"
        )

        self.assertEqual(response.status_code, 200)

    def test_staff_cannot_create(self):

        self.client.force_authenticate(
            user=self.staff_user
        )

        response = self.client.post(
            "/api/bookings/",
            {
                "patient_name": "Ram",
                "equipment_name": "Walker"
            },
            format="json"
        )

        self.assertEqual(response.status_code, 403)

    def test_staff_cannot_update(self):

        self.client.force_authenticate(
            user=self.staff_user
        )

        response = self.client.put(
            f"/api/bookings/{self.booking.id}/",
            {
                "patient_name": "Updated",
                "equipment_name": "Walker"
            },
            format="json"
        )

        self.assertEqual(response.status_code, 403)

    def test_staff_cannot_cancel(self):

        self.client.force_authenticate(
            user=self.staff_user
        )

        response = self.client.post(
            f"/api/bookings/{self.booking.id}/cancel/"
        )

        self.assertEqual(response.status_code, 403)

    def test_staff_can_mark_done(self):

        self.client.force_authenticate(
            user=self.staff_user
        )

        response = self.client.post(
            f"/api/bookings/{self.booking.id}/mark-done/"
        )

        self.assertEqual(response.status_code, 200)

    def test_viewer_cannot_create(self):

        self.client.force_authenticate(
            user=self.viewer_user
        )

        response = self.client.post(
            "/api/bookings/",
            {
                "patient_name": "Ram",
                "equipment_name": "Walker"
            },
            format="json"
        )

        self.assertEqual(response.status_code, 403)

    def test_viewer_cannot_update(self):

        self.client.force_authenticate(
            user=self.viewer_user
        )

        response = self.client.put(
            f"/api/bookings/{self.booking.id}/",
            {
                "patient_name": "Updated",
                "equipment_name": "Walker"
            },
            format="json"
        )

        self.assertEqual(response.status_code, 403)

    def test_viewer_cannot_cancel(self):

        self.client.force_authenticate(
            user=self.viewer_user
        )

        response = self.client.post(
            f"/api/bookings/{self.booking.id}/cancel/"
        )

        self.assertEqual(response.status_code, 403)

    def test_viewer_cannot_mark_done(self):

        self.client.force_authenticate(
            user=self.viewer_user
        )

        response = self.client.post(
            f"/api/bookings/{self.booking.id}/mark-done/"
        )

        self.assertEqual(response.status_code, 403)
    
    def test_admin_can_list(self):

        self.client.force_authenticate(
        user=self.admin_user
    )

        response = self.client.get(
        "/api/bookings/"
    )

        self.assertEqual(response.status_code, 200)


    def test_admin_can_retrieve(self):

        self.client.force_authenticate(
        user=self.admin_user
    )

        response = self.client.get(
        f"/api/bookings/{self.booking.id}/"
    )

        self.assertEqual(response.status_code, 200)


    def test_staff_can_list(self):

        self.client.force_authenticate(
        user=self.staff_user
    )

        response = self.client.get(
        "/api/bookings/"
    )

        self.assertEqual(response.status_code, 200)


    def test_staff_can_retrieve(self):

        self.client.force_authenticate(
        user=self.staff_user
    )

        response = self.client.get(
        f"/api/bookings/{self.booking.id}/"
    )

        self.assertEqual(response.status_code, 200)


    def test_viewer_can_list(self):

        self.client.force_authenticate(
        user=self.viewer_user
    )

        response = self.client.get(
        "/api/bookings/"
    )

        self.assertEqual(response.status_code, 200)


    def test_viewer_can_retrieve(self):

        self.client.force_authenticate(
        user=self.viewer_user
    )

        response = self.client.get(
        f"/api/bookings/{self.booking.id}/"
    )

        self.assertEqual(response.status_code, 200)

# Create your tests here.
