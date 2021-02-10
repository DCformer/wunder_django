from django import forms  
from rest_framework import serializers
from perfil_wunder.models import Correos_wunder 

class Correos_wunderSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Correos_wunder  
        fields = "__all__"  