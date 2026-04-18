from django.urls import path

from community.views import (CollectionListView,
                             CollectionDetailView,
                             CollectionCreateView,
                             CollectionUpdateView,
                             CollectionDeleteView
                             )

urlpatterns = (
    path('collections/', CollectionListView.as_view(), name='collection-list'),
    path('collections/create/', CollectionCreateView.as_view(), name='collection-create'),
    path('collections/<int:pk>/', CollectionDetailView.as_view(), name='collection-details'),
    path('collections/<int:pk>/edit/', CollectionUpdateView.as_view(), name='collection-edit'),
    path('collections/<int:pk>/delete/', CollectionDeleteView.as_view(), name='collection-delete'),
)
