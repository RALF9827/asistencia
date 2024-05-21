from django.db import models #libreria para realizar los modelos
from django.contrib.auth.models import User #libreria es para acceder al modelo interno de usuario en django
import datetime 

# Create your models here.

#clase de usuario traida de la libreria User
class usuario(User):
    class Meta:
        proxy = True
    
    def __str__(self):
        return f'{self.last_name} {self.first_name}'

#clase que crea el modelo materias en la base de datos
class Materia(models.Model):
    Codigo = models.CharField(max_length=6, unique=True, null=False, blank=False)
    Nombre = models.CharField(max_length=30, null=False, blank=False)
    
    #se usa para definir opciones internas del modelo en la base de datos
    class Meta:
        db_table = 'Materia'
    
    #funcion que define una referencia externa para llaves foraneas
    #puede ser cualquier columna del modelo
    def __str__(self):
        return f'{self.Codigo}-{self.Nombre}'

#models.Foreignkey es la llave foranea a otro modelo
class Profesores(models.Model):
    Cedula_id = models.CharField(max_length=10, unique=True, null=False, blank=False)
    Nombre = models.CharField(max_length=25, null=False, blank=False)
    Apellido = models.CharField(max_length=25, null=False, blank=False)
    Correo = models.CharField(max_length=40, null=False, blank=False)
    Telefono = models.CharField(max_length=10, null=False, blank=False)
    id_usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        db_table = 'Profesores'

    def __str__(self):
        return self.Cedula_id

class Alumnos(models.Model):
    Cedula_id = models.CharField(max_length=10, unique=True, null=False, blank=False)
    Nombre = models.CharField(max_length=25, null=False, blank=False)
    Apellido = models.CharField(max_length=25, null=False, blank=False)
    Correo = models.CharField(max_length=40, null=False, blank=False)
    Telefono = models.CharField(max_length=10, null=False, blank=False)
    id_usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        db_table = 'Alumnos'
    
    def __str__(self):
        return self.Cedula_id

#relacionaba que profesor da la materia
class Materia_X_Profesor(models.Model):
    Codigo = models.CharField(max_length=6, unique=True, null=False, blank=False)
    id_materia = models.ForeignKey(Materia, on_delete=models.DO_NOTHING, db_column='id_materia')
    id_profesor = models.ForeignKey(Profesores, on_delete=models.DO_NOTHING, db_column='id_profesor')

    class Meta:
        db_table = 'materiasXprofesor'
    
    def __str__(self):
        return self.Codigo

#relacionaba el alumno correspondiente a la materia y el profesor
class Alumnos_X_Materia_X_Profesor(models.Model):
    id_alumno = models.ForeignKey(Alumnos, on_delete=models.DO_NOTHING, db_column='id_alumno')
    id_mat_prof = models.ForeignKey(Materia_X_Profesor, on_delete=models.DO_NOTHING, db_column='id_mat_prof')

    class Meta:
        db_table = 'alumnosXmateria'

    def __int__(self):
        return self.pk

def ruta_qr(instance, filename):
    return f'QR-{instance.pk}-{filename}'

class QR(models.Model):
    Texto_qr = models.TextField(null=False, blank=False, unique=True)
    id_usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False, blank=False, editable=False, db_column='id_usuario')
    id_alum_mat_prof = models.ForeignKey(Alumnos_X_Materia_X_Profesor, on_delete=models.DO_NOTHING, editable=False, db_column='id_alum_mat_prof')
    direccion = models.ImageField(upload_to=ruta_qr, null=False, blank=False)
    fecha_generado = models.DateTimeField(null=False, blank=False, editable=False, default=datetime.datetime.now())
    usado = models.BooleanField(default=False, null=False, editable=False)

    class Meta:
        db_table = 'QR'

#no se utilizo iba a controlar las asistencias, pero se dejo en el qr
class Asistencia_X_Alumno(models.Model):
    id_alum_mat_prof = models.ForeignKey(Alumnos_X_Materia_X_Profesor, on_delete=models.DO_NOTHING, db_column='id_alum_mat_prof')
    id_qr = models.ForeignKey(QR, on_delete=models.DO_NOTHING, db_column='id_qr')

    class Meta:
        db_table = 'asistenciaXalumno'
