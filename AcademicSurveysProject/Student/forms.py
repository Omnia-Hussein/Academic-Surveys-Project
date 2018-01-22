from django.forms import ModelForm
from .models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = (
            'username',
            'password',
            'id_number',
            'name',
            'mobile_number',
            'primary_email',
            'secondary_email',
            'type',
        )
