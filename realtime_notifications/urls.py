from django.contrib import admin
from django.urls import include, path

from api import routing as notifications_routing

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("", include(notifications_routing.websocket_urlpatterns)),
]
