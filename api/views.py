from rest_framework import generics, permissions
from sightings.models import Sighting
from api.serializers import SightingSerializer


class SightingListAPIView(generics.ListAPIView):
    serializer_class = SightingSerializer

    def get_queryset(self):
        return Sighting.objects.filter(
            status=Sighting.StatusChoices.PUBLISHED,
            visibility=Sighting.VisibilityChoices.PUBLIC,
        )


class SightingDetailAPIView(generics.RetrieveAPIView):
    serializer_class = SightingSerializer

    def get_queryset(self):
        return Sighting.objects.filter(
            status=Sighting.StatusChoices.PUBLISHED,
            visibility=Sighting.VisibilityChoices.PUBLIC,
        )


class SightingCreateAPIView(generics.CreateAPIView):
    serializer_class = SightingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

