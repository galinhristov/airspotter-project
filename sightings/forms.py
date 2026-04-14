from django import forms
from sightings.models import Sighting

class BaseSightingForm(forms.ModelForm):
    class Meta:
        model = Sighting
        fields = (
            'title',
            'description',
            'spotted_at',
            'aircraft',
            'airport',
            'tags',
            'status',
            'visibility',
        )
        labels = {
            'title': 'Title',
            'description': 'Description',
            'spotted_at': 'Spotted at',
            'aircraft': 'Aircraft',
            'airport': 'Airport',
            'tags': 'Tags',
            'status': 'Publication status',
            'visibility': 'Visibility',
        }
        help_texts = {
            'title': 'Give your sighting a short and clear title.',
            'description': 'Describe what you saw.',
            'spotted_at': 'Select the exact date and time of the sighting.',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter sighting title'}),
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Describe the sighting'}),
            'spotted_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class SightingCreateForm(BaseSightingForm):
    pass


class SightingEditForm(BaseSightingForm):
    pass


class SightingDeleteForm(BaseSightingForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.disabled = True
