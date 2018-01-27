from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from Home.models import User


class UserCreate(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'name',
            'id_number',
            'mobile_number',
        )


class UserUpdate(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'name',
            'id_number',
            'mobile_number',
            'password',
        )
