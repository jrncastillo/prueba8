from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    #path('agregar/', views.agregar, name='agregar'),
    #path('agregar/agregarregistro/', views.agregarregistro, name='agregarregistro'),
    #path('eliminar/<int:id>', views.eliminar, name='eliminar'), #obtiene el id como argumento
    #path('actualizar/<int:id>', views.actualizar, name='actualizar'),
    #path('actualizarregistro/<int:id>', views.actualizarregistro, name='actualizarregistro'),


]