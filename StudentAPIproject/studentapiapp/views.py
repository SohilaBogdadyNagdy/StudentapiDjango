from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from studentapiapp.models import Student
from studentapiapp import serializers
from studentapiapp.serializers import StudentSerializer

# Create your views here.
@api_view(['GET'])
def student_get(request):
    if request.method == 'GET':
        s = Student.objects.all()
        serializer = StudentSerializer(s, many=True)
        return Response(serializer.data)
@api_view(['POST'])
def post_student (request):
    print (request.data)
    print (type (request.data))
    sname= request.data['name']
    saddress= request.data['address']
    newstudent = Student (name=sname,address=saddress)
    print (newstudent.id)
    newstudent.save ()
    return Response("student saved")
@api_view(['DELETE'])
def removestudent(request,pk):
    print ("in remove ")
    print (request.data)
    print (pk)
    instance = Student.objects.get(id=pk)
    instance.delete()
    return Response("delete operation done")

