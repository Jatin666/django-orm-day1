# we are using this to convert dict to json
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        field = "__all__"
