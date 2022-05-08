from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Task
from .serializer import TodoSerializer


# Create your views here.


class TodoView(APIView):
    def get(self, request):
        todo = Task.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


