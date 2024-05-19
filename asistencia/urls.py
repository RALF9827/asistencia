from django.contrib.auth.views import LoginView, logout_then_login, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('accounts/login/', LoginView.as_view(), {'template_name':'Login.html'}, name='ingreso'),
    path('Logout/', LogoutView.as_view(), name='logout'),

    path('registro/', views.Registro.as_view(), name='registro_usuario')
]