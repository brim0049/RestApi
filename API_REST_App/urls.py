from django.urls import path, include
from rest_framework import routers

from .views import VilleViewSet,login,logout, ReservationsViewSet, ChambreViewSet, UserViewSet, RoomViewSet, ReservationViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v1.0",
        description="Gestion de l'API",
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register("towns", VilleViewSet, basename="/")
router.register("reservations", ReservationsViewSet, basename="/")
router.register("reservation", ReservationViewSet, basename="/")
router.register("rooms", ChambreViewSet, basename="/" )
router.register("room", RoomViewSet, basename="/" )
router.register("user", UserViewSet, basename="/" )

urlpatterns = [
    path('', include(router.urls), name="towns"),
    path('', include(router.urls), name="reservation"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path("swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]