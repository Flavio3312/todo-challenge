from django.shortcuts import render
from django.http import JsonResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Tarea
# Create your views here.
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/lista-tarea/',
		'Detail View':'/detalle-tarea/<str:nombre>/',
		'Create':'/crear-tarea/',
		'Update':'/actualizar-tarea/<str:pk>/',
		'Delete':'/eliminar-tarea/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def getLista(request):
	try:
		tareas = Tarea.objects.all()
		serializer = TaskSerializer(tareas, many=True)
		return Response(serializer.data)
	except Tarea.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getTareas(request, nombre):
	
	try:
		nombre = nombre.lower()    	
		tareas = Tarea.objects.get(nombre=nombre)
		serializer = TaskSerializer(tareas, many=False)
		return Response(serializer.data)
	except Tarea.DoesNotExist:
		return JsonResponse({'message':'La tarea no existe'}, status=status.HTTP_404_NOT_FOUND)




@api_view(['POST'])
def setTarea(request):

	try:
		nombre = request.data['nombre'].lower()
		titulo = request.data['titulo']
		tarea = Tarea.objects.get(nombre=nombre, titulo=titulo)
		return Response({"message":"La tarea ya existe"}, status=status.HTTP_400_BAD_REQUEST)
	except Tarea.DoesNotExist:
		serializer = TaskSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	
		



		

@api_view(['GET'])
def actualizarTarea(request, pk):

	try:
		tarea = Tarea.objects.get(id=pk)
		tarea.completada = not tarea.completada
		tarea.save()
		serializer = TaskSerializer(tarea, many=False)
		return Response(serializer.data)

	except Tarea.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
		



@api_view(['DELETE'])
def eliminarTarea(request,pk):
  

	try:
		tareas = Tarea.objects.get(id=pk)
		tareas.delete()
		return Response('Item succsesfully delete!')
	except Tarea.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	



