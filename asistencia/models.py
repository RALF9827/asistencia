from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class usuario(User):
    class Meta:
        proxy = True
    
    def __str__(self):
        return f'{self.last_name} {self.first_name}'

class Materia(models.Model):
    pass
