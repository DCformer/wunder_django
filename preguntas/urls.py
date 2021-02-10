
from django.urls import include, path
from . import views

urlpatterns = [
  path('getpreguntas', views.get_preguntas),
  path('addpregunta', views.add_pregunta),
  path('updatepregunta/<int:pregunta_id>', views.update_pregunta),
  path('deletepregunta/<int:pregunta_id>', views.delete_pregunta)
]