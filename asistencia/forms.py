from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . import models

#formulario de creacion par ausuarios nuevos
class F_usuario(UserCreationForm):
    class Meta: #clase meta permite obtener el modelo al que ara referencia el formulario
        model = User #llama el modelo que se usara en el formulario
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']
        #fields se llaman las variables del modelo se puede llamar con una lista o con
        #'__all__' que traera todas las variables del modelo

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

