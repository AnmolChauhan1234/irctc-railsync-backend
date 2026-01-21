from django.contrib import admin
from .models import Train


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "train_number",
        "name",
        "source",
        "destination",
        "departure_time",
        "available_seats",
    )
    search_fields = ("train_number", "name", "source", "destination")
    list_filter = ("source", "destination")
