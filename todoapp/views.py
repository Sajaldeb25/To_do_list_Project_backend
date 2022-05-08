from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Task
from .serializer import TodoSerializer


class TodoView(APIView):
    def get(self, request):
        todo = Task.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request,format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailView(APIView):
    def get(self, request, pk):
        todo = Task.objects.get(id=pk)
        serializer = TodoSerializer(todo, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


