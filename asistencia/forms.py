from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . import models

class F_usuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

class F_Materia(forms.ModelForm):
    class Meta:
        model = models.Materia
        fields = '__all__'

class F_Profesores(forms.ModelForm):
    class Meta:
        model = models.Profesores
        fields = '__all__'

class F_Alumnos(forms.ModelForm):
    class Meta:
        model = models.Alumnos
        fields = '__all__'

class F_Materia_X_Profesor(forms.ModelForm):
    class Meta:
        model = models.Materia_X_Profesor
        fields = '__all__'

class F_Alumnos_X_Materia_X_Profesor(forms.ModelForm):
    class Meta:
        model = models.Alumnos_X_Materia_X_Profesor
        fields = '__all__'

