from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
#read operation
@api_view(['GET'])
def Booklist(request):
    booksobj=BookModel.objects.all()
    serializer=BookSerializer(booksobj,many=True)
    return Response(serializer.data)

#create  operation
@api_view(['POST'])
def post_book(request):
    booksobj=BookModel.objects.all()
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#update operation
@api_view(['POST'])
def update_book(request,id):
    booksobj=BookModel.objects.get(id=id)
    serializer=BookSerializer(instance=booksobj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#delete operation
@api_view(['DELETE'])
def delete_book(request,id):
    booksobj=BookModel.objects.get(id=id)
    booksobj.delete()
    return Response('book deleted successfully')