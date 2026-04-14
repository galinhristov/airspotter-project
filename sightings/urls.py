from django.urls import path

from sightings.views import (
    SightingListView,
    SightingDetailView,
    SightingCreateView,
    SightingUpdateView,
    SightingDeleteView,
)

urlpatterns = (
    path('', SightingListView.as_view(), name='sighting-list'),
    path('create/', SightingCreateView.as_view(), name='sighting-create'),
    path('<int:pk>/', SightingDetailView.as_view(), name='sighting-details'),
    path('<int:pk>/edit/', SightingUpdateView.as_view(), name='sighting-edit'),
    path('<int:pk>/delete/', SightingDeleteView.as_view(), name='sighting-delete'),
)
