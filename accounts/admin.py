from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import AirSpotterUser


@admin.register(AirSpotterUser)
class AirSpotterUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('display_name', 'bio', 'avatar', 'country'),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('display_name', 'bio', 'avatar', 'country'),
        }),
    )

    list_display = (
        'username',
        'email',
        'display_name',
        'country',
        'is_staff',
        'is_superuser',
    )
    search_fields = ('username', 'email', 'display_name', 'country')
