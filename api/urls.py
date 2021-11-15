from django.urls import path,re_path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('lista-tarea/', views.getLista, name="lista-tarea"),
    re_path(r'^detalle-tarea/(?P<nombre>[a-zA-Z0-9]+)$', views.getTareas, name="detalle-tarea"),
	path('crear-tarea/', views.setTarea, name="crear-tarea"),   
	path('actualizar-tarea/<str:pk>/', views.actualizarTarea, name="actualizar-tarea"),
	path('eliminar-tarea/<str:pk>/', views.eliminarTarea, name="eliminar-tarea"),
		
]