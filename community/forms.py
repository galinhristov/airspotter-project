from django import forms
from community.models import Collection

class BaseCollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = (
            'title',
            'description',
            'sightings',
            'is_public',
        )
        labels = {
            'title': 'Title',
            'description': 'Description',
            'is_public': 'Public collection',
        }
        help_texts = {
            'title': 'Choose a short and clear collection title.',
            'description': 'Optional description for this collection.',
            'sightings': 'Select sightings to include in the collection.',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter collection title'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe this collection'}),
        }


class CollectionCreateForm(BaseCollectionForm):
    pass


class CollectionEditForm(BaseCollectionForm):
    pass

class CollectionDeleteForm(BaseCollectionForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.disabled = True