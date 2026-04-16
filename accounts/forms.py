from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

UserModel = get_user_model()

class AirSpotterUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = (
            'username',
            'email',
            'display_name',
            'country',
            'password1',
            'password2',
        )
        labels = {
            'username': 'Username',
            'email': 'Email address',
            'display_name': 'Display name',
            'country': 'Country',
            'password1': 'Password',
            'password2': 'Confirm password',
        }
        help_texts = {
            'username': 'Choose a unique username.',
            'email': 'Enter a valid email address.',
            'display_name': 'Optional public display name.',
            'country': 'Optional country of origin.',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'display_name': forms.TextInput(attrs={'placeholder': 'Enter display name'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter country'}),
        }



class AirSpotterLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter username'}),
        label='Username',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
        label='Password',
    )



class AirSpotterUserEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = (
            'email',
            'display_name',
            'bio',
            'avatar',
            'country',
        )
        labels = {
            'email': 'Email address',
            'display_name': 'Display name',
            'bio': 'Bio',
            'avatar': 'Profile picture',
            'country': 'Country',
        }
        help_texts = {
            'bio': 'Tell the community a little about yourself.',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'display_name': forms.TextInput(attrs={'placeholder': 'Enter display name'}),
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write a short bio'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter country'}),
        }

