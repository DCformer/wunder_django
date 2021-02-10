from django import forms  
from rest_framework import serializers
from solicitudes_encuestas.models import Solicitud 

class SolicitudSerializer(serializers.ModelSerializer):  
    class Meta:  
        model =   Solicitud
        fields = "__all__"  