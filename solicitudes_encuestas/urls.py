from django.urls import include, path
from . import views

urlpatterns = [
  path('getsolicitudes', views.get_solicitudes),
  path('addsolicitud', views.add_solicitud),
  path('updatesolicitud/<int:solicitud_id>', views.update_solicitud),
  path('deletesolicitud/<int:solicitud_id>', views.delete_solicitud)
]