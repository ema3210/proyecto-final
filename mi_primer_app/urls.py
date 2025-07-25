from django.urls import path
from .views import (crear_familiar, inicio, crear_curso,crear_estudiante, buscar_cursos ,cursos
                   ,AutoCreateView, AutoListView, AutoDeleteView, AutoDetailView, AutoUpdateView)

urlpatterns = [
    path('',inicio,  name='inicio'),
    path('crear-familiar/', crear_familiar),
    path('crear-curso/', crear_curso, name='crear-curso'),
    path('crear-estudiante/', crear_estudiante, name='crear-estudiante'),
    path('cursos/', cursos, name='cursos'),
    path('cursos/buscar/', buscar_cursos, name='buscar-cursos'),
    
    
    #urls con vistas basadas en clase
    path('listar-autos/', AutoListView.as_view(), name='listar-autos'),
    path('crear-auto/', AutoCreateView.as_view(), name='crear-auto'),
    path('detalle-auto/<int:pk>/', AutoDetailView.as_view(), name='detalle-auto'),
    path('editar-auto/<int:pk>/', AutoUpdateView.as_view(), name='editar-auto'),
    path('eliminar-auto/<int:pk>/', AutoDeleteView.as_view(), name='eliminar-auto'),
]

