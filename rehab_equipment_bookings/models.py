from django.db import models
from django.contrib.auth.models import User

class UserRole(models.Model):

    ROLE_CHOICES = [
        ('admin','Admin'),
        ('assigned_staff','Assigned Staff'),
        ('viewer','Viewer'),
    ]
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices = ROLE_CHOICES
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
class RehabEquipmentBooking(models.Model):

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('cancelled', 'Cancelled'),
        ('done', 'Done'),
    ]

    patient_name = models.CharField(max_length=100)

    equipment_name = models.CharField(max_length=100)

    assigned_staff = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.patient_name



    


