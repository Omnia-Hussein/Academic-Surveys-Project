from django.db import models
from django.contrib.auth.models import User


# Professor Model
class Professor(models.Model):
    user = models.OneToOneField( User, primary_key=True,on_delete=models.CASCADE,)
    id_number = models.CharField( max_length=30,unique=True, verbose_name='ID number', )
    name = models.CharField(max_length=100, unique=True,)
    mobile_number = models.CharField(max_length=15,)
    secondary_email = models.EmailField( max_length=100,)


    @property
    def __str__(self):
        return self.name
