from pickle import GET
from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from accounts.models import EmpData
from accounts.serilizers import EmpDataSerilizer

@api_view(['GET']) 
def ApiOverView(request):
    return Response('API calling')

@api_view(['GET'])
def Emplist(request):
    emp=EmpData.objects.all()
    serilizer=EmpDataSerilizer(emp,many=True)
    return Response(serilizer.data)
