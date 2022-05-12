import random

from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Task, Article
from .serializer import TodoSerializer


class TodoView(APIView):
    def get(self, request):
        todo = Task.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
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


class TodoUpdateView(APIView):
    def post(self, request, pk):
        Task.objects.filter(id=pk).update(title=request.data['title'])
        return Response({'msg': 'Data updated.'}, status=status.HTTP_200_OK)


class ToDoDeleteView(APIView):
    def delete(self, request, pk):
        try:
            todo = Task.objects.get(pk=pk)
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({'msg': 'Does not exist'}, status=status.HTTP_404_NOT_FOUND)


class TodoCompletedView(APIView):
    def post(self, request, pk):
        Task.objects.filter(id=pk).update(completed=request.data['completed'])
        return Response({'msg': 'Data updated.'}, status=status.HTTP_200_OK)


def home_view(request):
    number = random.randint(1, 5)
    article = Article.objects.get(id=number)
    name = "sajal"
    h1_str = f"""
    <h1> Hello {name}, {number}, {article.title}, { article.content} </h1>
    """

    return HttpResponse(h1_str)

