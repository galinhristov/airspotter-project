from django.contrib.auth.models import AbstractUser
from django.db import models

class AirSpotterUser(AbstractUser):
    display_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    bio = models.TextField(
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
    )
    country = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.display_name or self.username