from django.core.exceptions import ValidationError
from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.utils.text import slugify


def validate_spotted_at_not_far_in_future(value):
    now = timezone.now()
    if value > now + timedelta(hours=2):
        raise ValidationError('Sighting time cannot be too far in the future.')


class Tag(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    class Meta:
        ordering = ('name',)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Sighting(models.Model):
    
    class StatusChoices(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'


    class VisibilityChoices(models.TextChoices):
        PUBLIC = 'public', 'Public'
        PRIVATE = 'private', 'Private'


    title = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    spotted_at = models.DateTimeField(
        validators=[validate_spotted_at_not_far_in_future],
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    owner = models.ForeignKey(
        'accounts.AirSpotterUser',
        on_delete=models.CASCADE,
        related_name='sightings',
    )
    aircraft = models.ForeignKey(
        'aviation.Aircraft',
        on_delete=models.CASCADE,
        related_name='sightings',
    )
    airport = models.ForeignKey(
        'aviation.Airport',
        on_delete=models.CASCADE,
        related_name='sightings',
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='sightings',
    )
    status = models.CharField(
        max_length=10,
        choices=StatusChoices,
        default=StatusChoices.DRAFT,
    )
    visibility = models.CharField(
        max_length=10,
        choices=VisibilityChoices,
        default=VisibilityChoices.PUBLIC,
    )

    class Meta:
        ordering = ('-spotted_at',)

    def __str__(self):
        return self.title


class SightingPhoto(models.Model):
    image = models.ImageField(
        upload_to='sighting_photos/',
    )
    caption = models.CharField(
        max_length=120,
        blank=True,
        null=True,
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
    )
    sighting = models.ForeignKey(
        Sighting,
        on_delete=models.CASCADE,
        related_name='photos',
    )
    uploaded_by = models.ForeignKey(
        'accounts.AirSpotterUser',
        on_delete=models.CASCADE,
        related_name='uploaded_photos',
    )
    thumbnail = models.ImageField(
        upload_to='sighting_thumbnails/',
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('-uploaded_at',)

    def __str__(self):
        return f'Photo for {self.sighting.title}'