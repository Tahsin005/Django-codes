from . models import Student
from . serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer