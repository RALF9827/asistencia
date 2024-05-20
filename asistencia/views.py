import pyqrcode
from pyqrcode import QRCode
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import View, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models
from . import mixing
import datetime

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
    
class Alumnos(LoginRequiredMixin, mixing.Mx_Superuser, View):
    modelo = models.Alumnos
    formulario = forms.F_Alumnos
    plantilla = './administrador/alumnos.html'

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
            formulario.save()
            return redirect ('registro_alumnos')

class Profesores(LoginRequiredMixin, mixing.Mx_Superuser, View):
    modelo = models.Profesores
    formulario = forms.F_Profesores
    plantilla = './administrador/profesores.html'

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
            formulario.save()
        return redirect ('registro_alumnos')

#controla la logica de la vista de materias
class Materias(LoginRequiredMixin, mixing.Mx_Superuser, View):
    modelo = models.Materia
    formulario = forms.F_Materia
    plantilla = './administrador/materias.html'

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
            formulario.save()
        return redirect ('registro_materias')
    
#controla la logica de la vista materia por profesor
class Materia_X_Profesor(LoginRequiredMixin, mixing.Mx_Superuser, View):
    modelo = models.Materia_X_Profesor
    formulario = forms.F_Materia_X_Profesor
    plantilla = './administrador/materia_x_profesor.html'

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
            formulario.save()
        return redirect ('asignar_profesor')
    
#contrala la vista de materia por profesor
class Alumnos_X_Materia_X_Profesor(LoginRequiredMixin, mixing.Mx_Superuser, View):
    modelo = models.Alumnos_X_Materia_X_Profesor
    formulario = forms.F_Alumnos_X_Materia_X_Profesor
    plantilla = './administrador/alumnos_x_materia_x_profesor.html'

    def get_queryset(self):
        return self.modelo.objects.all()

    #el get context_data envia las variables que necesitamos enviar a la plantilla html
    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['consulta'] = self.get_queryset()
        contexto['formulario'] = self.formulario
        return contexto
    
    def get(self, request, *args, **kwargs):
        extra_contexto = {}
        extra_contexto['consulta'] = self.modelo.objects.all().filter(id_alumno__id_usuario__id=request.user.id)
        return render(request, self.plantilla, {'get_context':self.get_context_data(), 'extra_contexto':extra_contexto})
    
    def post(self, request, *args, **kwargs):
        formulario = self.formulario(request.POST)
        if formulario.is_valid():
            formulario.save()
        return redirect ('asignar_alumno')

class Listado_materias(LoginRequiredMixin, View):
    modelo = models.Alumnos_X_Materia_X_Profesor
    plantilla = 'listado_materias.html'

    def get_queryset(self):
        return self.modelo.objects.all()

    #el get context_data envia las variables que necesitamos enviar a la plantilla html
    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['consulta'] = self.get_queryset()
        return contexto
    
    def get(self, request, *args, **kwargs):
        extra_contexto = {}
        extra_contexto['consulta'] = self.modelo.objects.all().filter(id_alumno__id_usuario__id=request.user.id)
        return render(request, self.plantilla, {'get_context':self.get_context_data(), 'extra_contexto':extra_contexto})
    

class QR(LoginRequiredMixin, View):
    modelo = models.QR
    plantilla = 'esperaQr.html'
    
    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        try:
            max_id = self.modelo.objects.values('id').latest('id')
            mostrar = int(max_id['id'])
        except:
            print('alumno nuevo')

        fecha = datetime.datetime.now()
        f_fecha = fecha.strftime('%Y-%m')

        direccion_txt = f'http://192.168.2.94:8000/asistencia/QR/{mostrar + 1}_{f_fecha}/{id}'
        direccion_qr = f'{mostrar + 1}_{f_fecha}{id}.png'

        print(direccion_txt)

        generador_qr = pyqrcode.create(direccion_txt)
        generador_qr.png(f'media/{direccion_qr}', scale=10)

        self.modelo.objects.create(Texto_qr=direccion_txt, direccion=direccion_qr, id_usuario=models.usuario.objects.get(id=request.user.id), id_alum_mat_prof=models.Alumnos_X_Materia_X_Profesor.objects.get(id=id))

        return render(request, self.plantilla, {'id':id})
    
class QR_detector(LoginRequiredMixin, View):
    modelo = models.QR
    plantilla = 'qr.html'

    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        consulta = self.modelo.objects.values('direccion').filter(id_usuario=request.user.id, usado=False, id_alum_mat_prof=id).latest('id')
        contexto = consulta['direccion']
        return render(request, self.plantilla, {'consulta':contexto})
    
class QR_lector(LoginRequiredMixin, View):
    modelo = models.QR
    plantilla = 'qr.html'
    
    def get_queryset(self):
        return self.modelo.objects.all()
    
    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['consulta'] = self.get_queryset()
        return contexto
    
    def get(self, request, *args, **kwargs):
        texto = kwargs['text']
        id = kwargs['pk']

        texto_completo = f'http://192.168.2.94:8000/asistencia/QR/{texto}/{id}'

        max_id = self.modelo.objects.filter(id_usuario=request.user.id, usado=False, id_alum_mat_prof=id).values('Texto_qr', 'id', 'id_alum_mat_prof').latest('id')
        texto_leido = str(max_id['Texto_qr'])
        id_qr = int(max_id['id'])
        qr_usado = self.modelo.objects.get(id=id_qr)


        print(texto_completo)
        print(texto_leido)

        if texto_completo == texto_leido:
            print('correcto')
            qr_usado.usado = True
            qr_usado.save()

            return redirect('index')
    
        return render(request, self.plantilla, self.get_context_data())
    



