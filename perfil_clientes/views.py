from django.shortcuts import render
from perfil_clientes.models import Usuario_cliente, Empresa
from perfil_clientes.serializers import Usuario_clienteSerializer, EmpresaSerializer

from django.shortcuts import render, redirect  

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from django.http import HttpResponse, response
from django.http import JsonResponse
from django.core import serializers

import json
from django.core.exceptions import ObjectDoesNotExist

#  CRUD EMPRESAS ##################################################################################
###################################################################################################

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])  
def welcome(request):
    content = {"message": "Bienvenido a la creacion de empresas"}
    return JsonResponse(content)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_empresas(request):
    user = request.user.id
    empresas = Empresa.objects.filter()
    serializer = EmpresaSerializer(empresas, many=True)
    return JsonResponse({'empresas': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_empresa(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        empresa = Empresa.objects.create(
            rut=payload["rut"],
            nombre=payload["nombre"],
            telefono=payload["telefono"],
            personality=payload["nombre"],
        )
        serializer = EmpresaSerializer(empresa)
        return JsonResponse({'empresa': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Paso algo malo :('}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_empresa(request, empresa_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        empresa_item = Empresa.objects.filter(id=empresa_id)
        # returns 1 or 0
        empresa_item.update(**payload)
        empresa = Empresa.objects.get(id=empresa_id)
        serializer = EmpresaSerializer(empresa)
        return JsonResponse({'empresa': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Paso algo malo :('}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_empresa(request, empresa_id):
    user = request.user.id
    try:
        empresa = Empresa.objects.get(id=empresa_id)
        empresa.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#  CRUD USUARIOS CLIENTES #########################################################################
###################################################################################################

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])  
def welcome(request):
    content = {"message": "Bienvenido a la creacion del perfil de los clientes"}
    return JsonResponse(content)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_usuarios_cliente(request):
    user = request.user.id
    usuarios_cliente = Usuario_cliente.objects.filter()
    serializer = Usuario_clienteSerializer(usuarios_cliente, many=True)
    return JsonResponse({'usuarios_cliente': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_usuario_cliente(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        empresa = Empresa.objects.get(id=payload["empresa"])
        usuario_cliente = Usuario_cliente.objects.create(
            nombre_usuario=payload["nombre_usuario"],
            clave=payload["clave"],
            correo=payload["correo"],
            empresa=empresa
        )
        serializer = Usuario_clienteSerializer(usuario_cliente)
        return JsonResponse({'usuario_cliente': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Paso algo malo :('}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_usuario_cliente(request, usuario_cliente_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        usuario_cliente_item = Usuario_cliente.objects.filter(id=usuario_cliente_id)
        # returns 1 or 0
        usuario_cliente_item.update(**payload)
        usuario_cliente = Usuario_cliente.objects.get(id=usuario_cliente_id)
        serializer = Usuario_clienteSerializer(usuario_cliente)
        return JsonResponse({'usuario_cliente': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Paso algo malo :('}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_usuario_cliente(request, usuario_cliente_id):
    user = request.user.id
    try:
        usuario_cliente = Usuario_cliente.objects.get(id=usuario_cliente_id)
        usuario_cliente.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)















