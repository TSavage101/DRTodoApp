from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from .models import Task

from .serializers import TaskSerializer

# Create your views here.
class AllTasks(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Task.objects.all()
        
        serializer = TaskSerializer(queryset, many=True)
        
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    
class SingleTask(APIView):
    def get(self, request, pk,*args, **kwargs):
        try:
            queryset = Task.objects.get(id=pk)
        except Task.DoesNotExist:
            return Response({'message': 'Task not found!'})
        
        serializer = TaskSerializer(queryset)
        
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        try:
            queryset = Task.objects.get(id=pk)
        except:
            return Response({'message': 'Task not found!'})
        
        serializer = TaskSerializer(instance=queryset, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def delete(self, request, pk, *args, **kwargs):
        try:
            queryset = Task.objects.get(id=pk)
        except:
            return Response({'message': 'Task not found!'})
        
        queryset.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)