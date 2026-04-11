from django.core.exceptions import ValidationError
from django.db import models

class Comment(models.Model):
    text = models.TextField(
        max_length=400,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    author = models.ForeignKey(
        'accounts.AirSpotterUser',
        on_delete=models.CASCADE,
        related_name='comments',
    )
    sighting = models.ForeignKey(
        'sightings.Sighting',
        on_delete=models.CASCADE,
        related_name='comments',
    )

    class Meta:
        ordering = ('-created_at',)

    def clean(self):
        if not self.text or not self.text.strip():
            raise ValidationError('Comment cannot be empty.')

    def __str__(self):
        return f'Comment by {self.author} on {self.sighting}'


class Collection(models.Model):
    title = models.CharField(
        max_length=80,
    )
    description = models.TextField(
        blank=True,
        null=True,
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
        related_name='collections',
    )
    sightings = models.ManyToManyField(
        'sightings.Sighting',
        blank=True,
        related_name='collections',
    )
    is_public = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ('title',)
        unique_together = ('owner', 'title')

    def __str__(self):
        return self.title