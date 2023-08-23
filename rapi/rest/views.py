from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .serializer import rstudentserializer
from .models import rstudent
# Create your views here.
@api_view(['GET'])
def getrstudent(request):
    Rstudent = rstudent.objects.all()
    serializer = rstudentserializer(Rstudent, many=True)
    return Response(serializer.data)
    
@api_view(['POST'])
def postrstudent(request):
    serializer = rstudentserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

