from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('aviation/', include('aviation.urls')),
    path('sightings/', include('sightings.urls')),
    path('community/', include('community.urls')),
    path('api/', include('api.urls')),
]
