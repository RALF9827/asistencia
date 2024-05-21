import pyqrcode
from pyqrcode import QRCode
from openpyxl import Workbook
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import View, DeleteView, UpdateView
from django.http import HttpRequest, HttpResponse
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

    #funcion que enviara la informacion que se podra mostrar en la plantilla html
    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['formulario'] = self.formulario
        return contexto
    
    #muestra la peticion get desde el navegador y renderiza la plantilla html
    def get(self, request, *args, **kwargs):
        return render(request, self.plantilla, self.get_context_data())
    
    #realiza la peticion post del navegador a la vista en declarada en python
    def post(self, request, *args, **kwargs):
        formulario = self.formulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            #usa esa informacion de la peticion post para iniciar sesion automaticamente
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
    plantilla = './usuario_alumno/listado_materias.html'

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

class Asistencias(View):
    modelo = models.QR
    plantilla = 'asistencias.html'

    def get(self, request, *args, **kwargs):
        contexto = {}
        contexto['consulta'] = self.modelo.objects.all().filter(usado=True)
        # contexto['consulta'] = self.modelo.objects.values('')
        return render(request, self.plantilla, {'contexto':contexto})
    
    def export_to_excel(request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="asistencias.xlsx"'

        wb = Workbook()
        ws = wb.active
        ws.title = "asistencias"

        # Add headers
        cabecera = ["alumno", "profesor", "codigo", "materia", "fecha asistencia"]
        ws.append(cabecera)

        #se realiza una consulta para obtener los datos a exportar
        excel_exportar = models.QR.objects.all().filter(usado=True)
        for excel in excel_exportar:
            ws.append([(excel.id_alum_mat_prof.id_alumno.Apellido +" "+ excel.id_alum_mat_prof.id_alumno.Nombre), (excel.id_alum_mat_prof.id_mat_prof.id_profesor.Apellido +" "+ excel.id_alum_mat_prof.id_mat_prof.id_profesor.Nombre), excel.id_alum_mat_prof.id_mat_prof.Codigo, excel.id_alum_mat_prof.id_mat_prof.id_materia.Nombre, str(excel.fecha_generado)])

        # Save the workbook to the HttpResponse
        wb.save(response)
        return response
    

class QR(LoginRequiredMixin, View):
    modelo = models.QR
    plantilla = 'esperaQr.html'
    
    #funcion get que al acceder a la vista genera automaticamente un qr nuevo para cada solicitud
    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        try:
            max_id = self.modelo.objects.values('id').latest('id') #retorna un diccionario
            mostrar = int(max_id['id']) #almacenas ese valor del diccionario
        except:
            print('alumno nuevo')

        fecha = datetime.datetime.now() #se obtiene la fecha actual con hora incluida
        f_fecha = fecha.strftime('%Y-%m') #se convierte esa fecah en un str con formato año-mes

        #direccion_txt es el texto que almacenara el codigo qr
        direccion_txt = f'http://192.168.18.87:8000/asistencia/QR/{mostrar + 1}_{f_fecha}/{id}' #cambiar la ip con la que se esta usando en el momento
        #direccion_qr es el nombre con el que se almacenara y guardara en la base de datos
        direccion_qr = f'{mostrar + 1}_{f_fecha}{id}.png'

        # print(direccion_txt)

        generador_qr = pyqrcode.create(direccion_txt)
        generador_qr.png(f'media/{direccion_qr}', scale=10)

        #crear el codigo qr y almacena la informacion en el modelo QR
        self.modelo.objects.create(Texto_qr=direccion_txt, direccion=direccion_qr, id_usuario=models.usuario.objects.get(id=request.user.id), id_alum_mat_prof=models.Alumnos_X_Materia_X_Profesor.objects.get(id=id))

        return render(request, self.plantilla, {'id':id})
    
class QR_detector(LoginRequiredMixin, View):
    modelo = models.QR
    plantilla = 'qr.html'

    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        #se valida que el qr sea el generado por el usuario correspondiente y siempre sera el ultimo qr generado por este mismo
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

        texto_completo = f'http://192.168.18.87:8000/asistencia/QR/{texto}/{id}'

        #se valida que el qr generado sea el mismo leido, llamando al ultimo que se genero
        max_id = self.modelo.objects.filter(id_usuario=request.user.id, usado=False, id_alum_mat_prof=id).values('Texto_qr', 'id', 'id_alum_mat_prof').latest('id')
        texto_leido = str(max_id['Texto_qr'])
        id_qr = int(max_id['id'])

        #obtener el id del modelo qr
        qr_usado = self.modelo.objects.get(id=id_qr)

        #se uso para validar si el qr era el mismo creado en pruebas
        # print(texto_completo)
        # print(texto_leido)

        #este if compara que el qr sea el ultimo que se genero y se escaneo
        if texto_completo == texto_leido:
            # print('correcto')
            qr_usado.usado = True #lo asigna en que ya se uso y lo guarda
            qr_usado.save()

            return redirect('index') #si el qr es valido mandara al index de lo contrario dara error
    
        return render(request, self.plantilla, self.get_context_data())
    



