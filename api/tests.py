from django.test import TestCase
from .models import Tarea

class TareaModelTest(TestCase):
    
        def test_tarea_is_published(self):
            tarea = Tarea(titulo='titulo', nombre='nombre')
            tarea.save()    
            self.assertEqual(tarea.titulo, 'titulo')
            self.assertEqual(tarea.nombre, 'nombre')
            self.assertEqual(tarea.creado, tarea.actualizado)
            self.assertFalse(tarea.completada)

      
            



