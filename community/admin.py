from django.contrib import admin

from community.models import Comment, Collection


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'sighting', 'created_at')
    search_fields = ('text',)
    list_filter = ('created_at',)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'is_public', 'created_at')
    search_fields = ('title', 'description',)
    list_filter = ('is_public',)
    filter_horizontal = ('sightings',)
