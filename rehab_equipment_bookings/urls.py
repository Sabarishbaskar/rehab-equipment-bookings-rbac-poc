from django.urls import path

from .views import (
    BookingListCreateView,
    BookingDetailView,
    CancelBookingView,
    MarkDoneView
)

urlpatterns = [

    path(
        'bookings/',
        BookingListCreateView.as_view()
    ),

    path(
        'bookings/<int:pk>/',
        BookingDetailView.as_view()
    ),

    path(
        'bookings/<int:pk>/cancel/',
        CancelBookingView.as_view()
    ),

    path(
        'bookings/<int:pk>/mark-done/',
        MarkDoneView.as_view()
    ),
]