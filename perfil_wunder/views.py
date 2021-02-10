from django.shortcuts import render
from perfil_wunder.models import Correos_wunder, Usuario_wunder
from perfil_wunder.serializers import Correos_wunderSerializer

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

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])  
def welcome(request):
    content = {"message": "Bienvenido a la creacion de los perfiles de wunder"}
    return JsonResponse(content)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_correos_wunder(request):
    user = request.user.id
    correos_wunder = Correos_wunder.objects.filter()
    serializer = Correos_wunderSerializer(correos_wunder, many=True)
    return JsonResponse({'correos_wunder': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_correo_wunder(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        usuario_wunder = Usuario_wunder.objects.get(id=payload["usuario_wunder"])
        correo_wunder = Correos_wunder.objects.create(
            email=payload["email"],
            clave=payload["clave"],
            usuario_wunder=usuario_wunder
        )
        serializer = Correos_wunderSerializer(correo_wunder)
        return JsonResponse({'correo_wunder': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Paso algo malo :('}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_correo_wunder(request, correo_wunder_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        correo_wunder_item = Correos_wunder.objects.filter(id=correo_wunder_id)
        # returns 1 or 0
        correo_wunder_item.update(**payload)
        correo_wunder = Correos_wunder.objects.get(id=correo_wunder_id)
        serializer = Correos_wunderSerializer(correo_wunder)
        return JsonResponse({'correo_wunder': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Paso algo malo :('}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_correo_wunder(request, correo_wunder_id):
    user = request.user.id
    try:
        correo_wunder = Correos_wunder.objects.get(id=correo_wunder_id)
        correo_wunder.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)