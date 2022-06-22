from rest_framework import viewsets
from . import models
from . import serilizers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset=models.EmpData.objects.all()
    serializer_class=serilizers.EmpDataSerilizer