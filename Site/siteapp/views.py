from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework .views import APIView

from .models import School
from .serializers import SchoolSerializer


#inbuilt module its like an framework

# Create your views here.

#django ORM to communicate with database
class Create(APIView):
    def post(self,request):
        name = request.data.get("name") #fetching the name from the request
        serializer = SchoolSerializer(data=request.data, many=False)
        school_count = School.objects.filter(name= name).count()#checking the school name exisit or not
        if school_count:
            return Response({"data":"School name already exist","status":status.HTTP_409_CONFLICT})
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data,"status":status.HTTP_201_CREATED})


