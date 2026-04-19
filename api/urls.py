from django.urls import path

from api.views import SightingListAPIView, SightingDetailAPIView, SightingCreateAPIView, AircraftListAPIView

urlpatterns = (
    path('sightings/', SightingListAPIView.as_view(), name='api-sightings-list'),
    path('sightings/<int:pk>/', SightingDetailAPIView.as_view(), name='api-sithings-detail'),
    path('sightings/create/', SightingCreateAPIView.as_view(), name='api-sightings-create'),
    path('aircraft/', AircraftListAPIView.as_view(), name='api-aircraft-list'),
)