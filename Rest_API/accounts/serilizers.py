from pyexpat import model
from rest_framework import serializers
from .models import EmpData

class EmpDataSerilizer(serializers.ModelSerializer):
    class Meta:
        model=EmpData
        fields='__all__'
