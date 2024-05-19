from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import View, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms

# Create your views here.

# def index(request):
#     template = 'index.html'
#     return render(request, template)

class index(LoginRequiredMixin, View):
    template = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template)
    
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
    
