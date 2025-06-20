from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, EventTicketViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'tickets', EventTicketViewSet, basename='ticket')

urlpatterns = [
    path('', include(router.urls)),
]