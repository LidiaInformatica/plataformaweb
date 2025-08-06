from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_estudiantes, name='lista_estudiantes'),
    path('<int:id>/', views.detalle_estudiante, name='detalle_estudiante'),
]