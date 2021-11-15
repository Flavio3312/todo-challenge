METODOS PARA OBTENER LOS DATOS DE LA API O CREAR UNA NUEVA LISTA DE TAREAS

PROBADOS CON POSTMAN:

GET   http://{$PATH}/api/lista-tarea (esta ruta permite listar todas las tareas)

GET   http://{$PATH}/api/detalle-tarea/{nombre} (esta ruta permite listar la tarea con el nombre)-cualquier string en mayusculas o minusculas

POST  http://{$PATH}/api/crear-tarea/ (esta ruta permite crear una tarea) - enviar un json con el nombre de la tarea y el titulo de la tarea por body en Postman ejemplo: ({

      "nombre": "nombre de la tarea",
      "titulo": "titulo de la tarea"

})



GET http://{$PATH}/api/actualizar-tarea/<str:pk>/ (esta ruta permite actualizar una tarea) - enviar un id de la tarea y pasa el estado de completada a True o Flase


DELETE http://{$PATH}/api/eliminar-tarea/<str:pk>/(esta ruta permite eliminar una tarea) - enviar un id de la tarea

#############################################################################################################################################################

Pasos 

1)Bajar el Repositorio de la API

2)Modificar constantes del .env de acuerdo a las configuracion de tu base de datos 


2)CREAR UN ENTORNO VIRTUAL E INSTALAR LOS PAQUETES DEL FICHERO requirements.txt

2.a)pip install virtualenv

2.b)venv\Scripts\activate.bat

2.c)pip install -r requirements.txt

3)CREAR TABLA Y COLUMNAS EN LA BASE DE DATOS

python manage.py makemigrations

python manage.py migrate

4)CREAR EL USUARIO ADMINISTRADOR

python manage.py createsuperuser
username : flavio
password : admin1234

5)CORRER TEST

python manage.py test

6)RUN SERVER
python manage.py runserver

revisar los endpoints de la api en el navegador para consumir con Django Rest Framework 


http://127.0.0.1:8000/api/

Api Overview 

GET /api/
HTTP 200 OK
Allow: GET, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "List": "/lista-tarea/",
    "Detail View": "/detalle-tarea/<str:nombre>/",
    "Create": "/crear-tarea/",
    "Update": "/actualizar-tarea/<str:pk>/",
    "Delete": "/eliminar-tarea/<str:pk>/"
}










