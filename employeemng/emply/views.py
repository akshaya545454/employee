from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import Empserial
from .models import Employee

# Create your views here.
class EmpModViewset(ModelViewSet):
    serializer_class=Empserial
    queryset=Employee.objects.all()
    model=Employee
