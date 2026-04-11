from django.contrib import admin

from sightings.models import Tag, Sighting, SightingPhoto


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)


@admin.register(Sighting)
class SightingAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'aircraft', 'airport', 'spotted_at', 'status', 'visibility')
    search_fields = ('title', 'description')
    list_filter = ('status', 'visibility', 'airport', 'aircraft')
    filter_horizontal = ('tags',)


@admin.register(SightingPhoto)
class SightingPhotoAdmin(admin.ModelAdmin):
    list_display = ('sighting', 'uploaded_by', 'uploaded_at')
    search_fields = ('caption',)


