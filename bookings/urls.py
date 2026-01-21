from django.urls import path
from .views import BookingCreateView, MyBookingsView

urlpatterns = [
    path("/", BookingCreateView.as_view()),
    path("my/", MyBookingsView.as_view()),
]
