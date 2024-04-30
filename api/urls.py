from django.urls import path

from .views import PublishView, SubscribeView

urlpatterns = [
    path("publish/", PublishView.as_view(), name="publish"),
    path("subscribe/", SubscribeView.as_view(), name="subscribe"),
]
