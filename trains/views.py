import time
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Train
from .serializers import TrainSerializer
from accounts.permissions import IsAdmin
from core.mongo import MongoService


class TrainAdminView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request):
        serializer = TrainSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # If updating existing train
        train_number = serializer.validated_data["train_number"]
        train, created = Train.objects.update_or_create(
            train_number=train_number,
            defaults=serializer.validated_data,
        )

        return Response(
            TrainSerializer(train).data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )


# class TrainSearchView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         start = time.time()

#         source = request.query_params.get("source")
#         destination = request.query_params.get("destination")

#         if not source or not destination:
#             return Response(
#                 {"error": "source and destination are required"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         qs = Train.objects.filter(
#             source__iexact=source,
#             destination__iexact=destination,
#         )

#         serializer = TrainSerializer(qs, many=True)

#         exec_time = int((time.time() - start) * 1000)

#         # Mongo logging
#         db = MongoService.get_db()
#         db["api_logs"].insert_one({
#             "endpoint": "/api/trains/search/",
#             "params": {"source": source, "destination": destination},
#             "user_id": request.user.id,
#             "execution_time_ms": exec_time,
#             "timestamp": datetime.utcnow(),
#         })

#         return Response(serializer.data)




class TrainSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        start = time.time()

        source = request.query_params.get("source")
        destination = request.query_params.get("destination")

        if not source or not destination:
            return Response(
                {"error": "source and destination are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        limit = int(request.query_params.get("limit", 10))
        offset = int(request.query_params.get("offset", 0))

        qs = Train.objects.filter(
            source__iexact=source,
            destination__iexact=destination,
        )

        total = qs.count()
        qs = qs[offset: offset + limit]

        serializer = TrainSerializer(qs, many=True)

        exec_time = int((time.time() - start) * 1000)

        # Mongo logging
        db = MongoService.get_db()
        db["api_logs"].insert_one({
            "endpoint": "/api/trains/search/",
            "params": {
                "source": source,
                "destination": destination,
                "limit": limit,
                "offset": offset,
            },
            "user_id": request.user.id,
            "execution_time_ms": exec_time,
            "timestamp": datetime.utcnow(),
        })

        return Response({
            "total": total,
            "limit": limit,
            "offset": offset,
            "results": serializer.data,
        })

