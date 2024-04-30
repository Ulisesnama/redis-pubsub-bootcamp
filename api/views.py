import redis
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from realtime_notifications import settings

redis_client = redis.StrictRedis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0
)


class PublishView(APIView):
    def post(self, request, *args, **kwargs):
        message = request.data.get("message", "")
        if message:
            redis_client.publish("notifications", message)
            return Response(
                {"status": "Message sent", "message": message},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"status": "Error", "message": "No message provided"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class SubscribeView(APIView):
    def get(self, request, *args, **kwargs):
        pubsub = redis_client.pubsub()
        pubsub.subscribe("notifications")

        for message in pubsub.listen():
            if message["type"] == "message":
                data = message["data"].decode("utf-8")
                return Response(
                    {"status": "Message Received", "message": data},
                    status=status.HTTP_200_OK,
                )
