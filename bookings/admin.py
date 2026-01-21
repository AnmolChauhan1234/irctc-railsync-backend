from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "train", "seats_booked", "created_at")
    search_fields = ("user__email", "train__train_number")
    list_filter = ("created_at",)
