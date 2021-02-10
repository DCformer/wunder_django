from django.urls import include, path
from . import views

urlpatterns = [
  path('getusuarios_clientes', views.get_usuarios_cliente),
  path('addusuario_cliente', views.add_usuario_cliente),
  path('updateusuario_cliente/<int:usuario_cliente_id>', views.update_usuario_cliente),
  path('deleteusuario_cliente/<int:usuario_cliente_id>', views.delete_usuario_cliente),

  path('getempresas', views.get_empresas),
  path('addempresas', views.add_empresa),
  path('updateempresas/<int:empresas_id>', views.update_empresa),
  path('deleteempresa/<int:empresa_id>', views.delete_empresa)
]