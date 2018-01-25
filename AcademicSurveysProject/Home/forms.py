from django.contrib.auth.forms import UserCreationForm
from Home.models import User


class UserForm(UserCreationForm):
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
