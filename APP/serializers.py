from dataclasses import field
from rest_framework import serializers
from .models import Teacher , Student , ClassRoom , College


class CollegeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  College
        fields = '__all__'


class ClasssRoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
