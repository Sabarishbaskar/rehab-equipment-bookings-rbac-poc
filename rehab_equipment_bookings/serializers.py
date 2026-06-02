from rest_framework import serializers
from .models import RehabEquipmentBooking


class RehabEquipmentBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = RehabEquipmentBooking
        fields = "__all__"