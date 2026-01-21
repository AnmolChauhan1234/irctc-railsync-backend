from django.db import transaction
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Booking
from .serializers import BookingCreateSerializer, BookingSerializer
from trains.models import Train


class BookingCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BookingCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        train_id = serializer.validated_data["train_id"]
        seats = serializer.validated_data["seats"]

        with transaction.atomic():
            try:
                # lock the row
                train = Train.objects.select_for_update().get(id=train_id)
            except Train.DoesNotExist:
                return Response(
                    {"error": "Train not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            if train.available_seats < seats:
                return Response(
                    {"error": "Not enough seats available"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # deduct seats
            train.available_seats -= seats
            train.save()

            booking = Booking.objects.create(
                user=request.user,
                train=train,
                seats_booked=seats,
            )

        return Response(
            BookingSerializer(booking).data,
            status=status.HTTP_201_CREATED,
        )


class MyBookingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        bookings = Booking.objects.filter(user=request.user).select_related("train")
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
