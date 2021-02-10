from django.shortcuts import render, redirect  
from solicitudes_encuestas.serializers import SolicitudSerializer
from solicitudes_encuestas.models import Solicitud 
from encuestas.models import Encuesta
from perfil_clientes.models import Usuario_cliente 
from perfil_wunder.models import Usuario_wunder 

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
    content = {"message": "Bienvenido a la creacion de la solicitud de encuestas"}
    return JsonResponse(content)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_solicitudes(request):
    user = request.user.id
    solicitudes = Solicitud.objects.all()
    serializer = SolicitudSerializer(solicitudes, many=True)
    return JsonResponse({'solicitudes': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_solicitud(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        id_encuesta = Encuesta.objects.get(id=payload["id_encuesta"])
        id_cliente = Usuario_cliente.objects.get(id=payload["id_cliente"])
        id_wunder = Usuario_wunder.objects.get(id=payload["id_wunder"])
        solicitud = Solicitud.objects.create(
            fecha=payload["fecha_solicitud"],
            estado=payload["fecha_solicitud"],
            puntaje_obtenido=payload["puntaje_obtenido"],
            id_encuesta=id_encuesta,
            id_cliente=id_cliente,
            id_wunder=id_wunder
        )
        serializer = SolicitudSerializer(solicitud)
        return JsonResponse({'solicitud': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_solicitud(request, solicitud_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        solicitud_item = Solicitud.objects.filter(id=solicitud_id)
        # returns 1 or 0
        solicitud_item.update(**payload)
        solicitud = Solicitud.objects.get(id=solicitud_id)
        serializer = SolicitudSerializer(solicitud)
        return JsonResponse({'solicitud': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_solicitud(request, solicitud_id):
    user = request.user.id
    try:
        solicitud = Solicitud.objects.get(id=solicitud_id)
        solicitud.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)