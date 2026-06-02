from rest_framework.response import Response
from rest_framework.views import APIView

from .models import RehabEquipmentBooking
from .serializers import RehabEquipmentBookingSerializer
from .permissions import RBACPermission


class BookingListCreateView(APIView):

    def get(self, request):
        self.action_name = "list"

        if not RBACPermission().has_permission(request, self):
            return Response(
                {"detail": "Forbidden"},
                status=403
            )

        bookings = RehabEquipmentBooking.objects.all()
        serializer = RehabEquipmentBookingSerializer(bookings, many=True)

        return Response(serializer.data)

    def post(self, request):
        self.action_name = "create"

        if not RBACPermission().has_permission(request, self):
            return Response(
                {"detail": "Forbidden"},
                status=403
            )

        serializer = RehabEquipmentBookingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class BookingDetailView(APIView):

    def get_object(self, pk):
        return RehabEquipmentBooking.objects.get(pk=pk)

    def get(self, request, pk):
        self.action_name = "retrieve"

        if not RBACPermission().has_permission(request, self):
            return Response(
                {"detail": "Forbidden"},
                status=403
            )

        booking = self.get_object(pk)

        serializer = RehabEquipmentBookingSerializer(booking)

        return Response(serializer.data)

    def put(self, request, pk):
        self.action_name = "update"

        if not RBACPermission().has_permission(request, self):
            return Response(
                {"detail": "Forbidden"},
                status=403
            )

        booking = self.get_object(pk)

        serializer = RehabEquipmentBookingSerializer(
            booking,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


class CancelBookingView(APIView):

    def post(self, request, pk):

        self.action_name = "cancel"

        if not RBACPermission().has_permission(request, self):
            return Response(
                {"detail": "Forbidden"},
                status=403
            )

        booking = RehabEquipmentBooking.objects.get(pk=pk)

        booking.status = "cancelled"
        booking.save()

        return Response(
            {"message": "Booking cancelled"}
        )


class MarkDoneView(APIView):

    def post(self, request, pk):

        self.action_name = "mark_done"

        if not RBACPermission().has_permission(request, self):
            return Response(
                {"detail": "Forbidden"},
                status=403
            )

        booking = RehabEquipmentBooking.objects.get(pk=pk)

        booking.status = "done"
        booking.save()

        return Response(
            {"message": "Booking marked done"}
        )


