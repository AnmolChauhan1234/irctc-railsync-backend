from rest_framework import serializers
from .models import Booking
from trains.serializers import TrainSerializer

class BookingCreateSerializer(serializers.Serializer):
    train_id = serializers.IntegerField()
    seats = serializers.IntegerField(min_value=1)


class BookingSerializer(serializers.ModelSerializer):
    train = TrainSerializer()

    class Meta:
        model = Booking
        fields = ["id", "train", "seats_booked", "created_at"]
