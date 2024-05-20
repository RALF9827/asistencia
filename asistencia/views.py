from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import View, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models

# Create your views here.

# def index(request):
#     template = 'index.html'
#     return render(request, template)

#se controla la logica de la vista principal index
class index(LoginRequiredMixin, View):
    plantilla = 'index.html'

    #define la accion del metodo get o mostrar al cargar la vista, renderiza el index.html
    def get(self, request, *args, **kwargs):
        return render(request, self.plantilla)
    
class notificaciones(View):
    plantilla = 'notificaciones.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.plantilla)
    
#se controla la logica de la vista de registro
class Registro(View):
    formulario = forms.F_usuario
    plantilla = 'registro.html'

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['formulario'] = self.formulario
        return contexto
    
    def get(self, request, *args, **kwargs):
        return render(request, self.plantilla, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        formulario = self.formulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
        return redirect('index')
    
class Alumnos(LoginRequiredMixin, View):
    modelo = models.Alumnos
    formulario = forms.F_Alumnos
    plantilla = 'alumnos.html'

    #el get context_data envia las variables que necesitamos enviar a la plantilla html
    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['formulario'] = self.formulario
        return contexto
    
    def get(self, request, *args, **kwargs):
        return render(request, self.plantilla, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        formulario = self.formulario(request.POST)
        if formulario.is_valid():
            formulario.save
        return redirect ('registro_alumnos')

class Profesores(LoginRequiredMixin, View):
    modelo = models.Profesores
    formulario = forms.F_Profesores
    plantilla = 'profesores.html'

    #el get context_data envia las variables que necesitamos enviar a la plantilla html
    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['formulario'] = self.formulario
        return contexto
    
    def get(self, request, *args, **kwargs):
        return render(request, self.plantilla, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        formulario = self.formulario(request.POST)
        if formulario.is_valid():
            formulario.save
        return redirect ('registro_alumnos')

#controla la logica de la vista de materias
class Materias(LoginRequiredMixin, View):
    modelo = models.Materia
    formulario = forms.F_Materia
    plantilla = 'materias.html'

    #el get context_data envia las variables que necesitamos enviar a la plantilla html
    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['formulario'] = self.formulario
        return contexto
    
    def get(self, request, *args, **kwargs):
        return render(request, self.plantilla, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        formulario = self.formulario(request.POST)
        if formulario.is_valid():
            formulario.save
        return redirect ('registro_materias')
    
#controla la logica de la vista materia por profesor
class Materia_X_Profesor(LoginRequiredMixin, View):
    modelo = models.Materia_X_Profesor
    formulario = forms.F_Materia_X_Profesor
    plantilla = 'materia_x_profesor.html'

    #el get context_data envia las variables que necesitamos enviar a la plantilla html
    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['formulario'] = self.formulario
        return contexto
    
    def get(self, request, *args, **kwargs):
        return render(request, self.plantilla, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        formulario = self.formulario(request.POST)
        if formulario.is_valid():
            formulario.save
        return redirect ('asignar_profesor')
    
#contrala la vista de materia por profesor
class Alumnos_X_Materia_X_Profesor(LoginRequiredMixin, View):
    modelo = models.Alumnos_X_Materia_X_Profesor
    formulario = forms.F_Alumnos_X_Materia_X_Profesor
    plantilla = 'alumnos_x_materia_x_profesor.html'

    def get_queryset(self):
        return self.modelo.objects.all()

    #el get context_data envia las variables que necesitamos enviar a la plantilla html
    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['formulario'] = self.formulario
        return contexto
    
    def get(self, request, *args, **kwargs):
        return render(request, self.plantilla, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        formulario = self.formulario(request.POST)
        if formulario.is_valid():
            formulario.save
        return redirect ('asignar_alumno')