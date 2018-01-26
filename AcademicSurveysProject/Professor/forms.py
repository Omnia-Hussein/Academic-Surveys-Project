from django import forms
from django.contrib.auth.forms import UserCreationForm
from Home.models import User
from .models import Professor


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Inform a valid email address.',
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class ProfForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = (
            'secondary_email',
        )
