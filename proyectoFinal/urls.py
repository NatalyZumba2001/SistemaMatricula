"""proyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app_estudiantes.views import * 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app_estudiantes.urls')),

    #VISTA ESTUDIANTE
    path('lista_estudiante/',login_required(ListaEstudiante.as_view()),name="listar_estudiante"),
    path('crea_estudiante/',login_required(CrearEstudiante.as_view()),name="crear_estudiante"),
    path('edita_estudiante/<int:pk>/',login_required(ActualizarEstudiante.as_view()),name="editar_estudiante"),
    path('elimina_estudiante/<int:pk>/',login_required(EliminarEstudiante.as_view()),name="eliminar_estudiante"),

    path('lista_pago/',login_required(ListaPago.as_view()),name="listar_pago"),
    path('crea_pago/',login_required(CrearPago.as_view()),name="crear_pago"),
    path('edita_pago/<int:pk>/',login_required(ActualizarPago.as_view()),name="editar_pago"),
    path('elimina_estudiante/<int:pk>/',login_required(EliminarEstudiante.as_view()),name="eliminar_pago"),


  
]





admin.site.site_header = 'SISTEMA DE GESTION DE MATRICULAS'