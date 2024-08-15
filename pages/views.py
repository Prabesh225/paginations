from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from .paginations import myoffsetpagination

class Student_details(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer  
    pagination_class = myoffsetpagination
    # pagination_class = CustomPageNumberPagination


# class Student_details(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     pagination_class =[CustomPageNumberPagination]