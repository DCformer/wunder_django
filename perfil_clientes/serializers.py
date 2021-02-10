from django import forms  
from rest_framework import serializers
from perfil_clientes.models import Usuario_cliente, Empresa

class Usuario_clienteSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Usuario_cliente  
        fields = "__all__"  

class EmpresaSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Empresa  
        fields = "__all__"  