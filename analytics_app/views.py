from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.mongo import MongoService


class TopRoutesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        db = MongoService.get_db()
        logs = db["api_logs"]

        pipeline = [
            {
                "$group": {
                    "_id": {
                        "source": "$params.source",
                        "destination": "$params.destination"
                    },
                    "count": {"$sum": 1}
                }
            },
            {"$sort": {"count": -1}},
            {"$limit": 5}
        ]

        result = list(logs.aggregate(pipeline))

        formatted = [
            {
                "source": r["_id"]["source"],
                "destination": r["_id"]["destination"],
                "count": r["count"],
            }
            for r in result
        ]

        return Response(formatted)
