from django.http.response import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import PreguntaSerializer
from .models import Pregunta
from rest_framework import status

from .models import Pregunta
import json
from django.core.exceptions import ObjectDoesNotExist


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])  
def welcome(request):
    content = {"message": "Bienvenido a la seccion de preguntas!"}
    return JsonResponse(content)

#Usuario puede obtener preguntas
@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_preguntas(request):
    user = request.user.id
    preguntas = Pregunta.objects.all()
    serializer = PreguntaSerializer(preguntas, many=True)
    return JsonResponse({'preguntas': serializer.data}, safe=False, status=status.HTTP_200_OK)


# Usuario puede agregar Preguntas
@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_pregunta(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        pregunta = Pregunta.objects.create(
            texto_pregunta = payload["Pregunta"],
            tipo_pregunta = payload["Tipo de pregunta"],
            alternativa = payload["Respuestas o alternativas"],
            estado = payload["Estado de la pregunta"],
            pub_date = payload["Fecha de la pregunta"], 
        )
        serializer = PreguntaSerializer(pregunta)
        return JsonResponse({'preguntas': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Mega error!!'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Uusario puede actualizar pregunta con el el ID
@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_pregunta(request, pregunta_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        pregunta_item = Pregunta.objects.filter(id=pregunta_id)
        # returns 1 or 0
        pregunta_item.update(**payload)
        pregunta = Pregunta.objects.get(id=pregunta_id)
        serializer = PreguntaSerializer(pregunta)
        return JsonResponse({'pregunta': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Mega error!!'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  

# Usuario puede borrar pregunta con el ID
@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_pregunta(request, pregunta_id):
    user = request.user.id
    try:
        pregunta = Pregunta.objects.get(id=pregunta_id)
        pregunta.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)