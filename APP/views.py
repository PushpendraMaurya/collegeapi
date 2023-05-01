from django.shortcuts import render
# from django.views import  View
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import ClassRoom, Student , College ,Teacher
from .serializers import ClasssRoomSerializer , StudentSerializer , CollegeSerializer , TeacherSerializer
# Create your views here.


class ClassRoomViewset(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClasssRoomSerializer
    permission_classes = [IsAuthenticated]


class StudentViewsets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class  = StudentSerializer
    permission_classes = [IsAuthenticated]

class CollegeViewsets(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]

class TeacherViewsets(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]
    



def students_view(request):
    data = Student.objects.all()
    context = {'data':data}
    return render(request, 'student.html' ,context)

def college_view(request):
    data = College.objects.all()
    context = {'data':data}
    return render(request, 'college.html' , context)

def teacher_view(request):
    data = Teacher.objects.all()
    context = {'data':data}
    return render(request,'teacher.html',context)

def classroom_view(request):
    data = ClassRoom.objects.all()
    context = {'data':data}
    return render(request,'classroom.html',context)
