from django.contrib.auth.views import LoginView, logout_then_login, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('accounts/login/', LoginView.as_view(), {'template_name':'Login.html'}, name='ingreso'),
    path('Logout/', LogoutView.as_view(), name='logout'),

    path('registro/', views.Registro.as_view(), name='registro_usuario'),
    path('notificaciones/', views.notificaciones.as_view(), name='notificaciones'),

    path('Registro_alumnos/', views.Alumnos.as_view(), name='registro_alumnos'),
    path('Registro_profesores/', views.Profesores.as_view(), name='registro_profesores'),
    path('Registro_materias/', views.Materias.as_view(), name='registro_materias'),
    path('Materia_x_profesor/', views.Materia_X_Profesor.as_view(), name='asignar_profesor'),
    path('Alumno_x_materia/', views.Alumnos_X_Materia_X_Profesor.as_view(), name='asignar_alumno'),
    path('QR/Detector/<int:pk>', views.QR.as_view(), name='generar_qr'),
    path('QR/Detector/QR_detector/<int:pk>', views.QR_detector.as_view(), name='detector_qr'),
    path('QR/<str:text>/<int:pk>', views.QR_lector.as_view(), name='qr_leido'),

    path('listado_materias/', views.Listado_materias.as_view(), name='listado_materias'),
    
]