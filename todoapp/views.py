import random

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Task, Article
from .serializer import TodoSerializer
from .forms import ArticleForm


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

    # my_lst = [12, 23, 30, 11, 67]
    articles = Article.objects.all()
    my_lst = articles
    my_lst_str = ""

    for i in my_lst:
        my_lst_str += f"Number is: {i}\n"

    context = {
        "my_lst_str": my_lst,
        "object": article,
        "id": article.id,
        "title": article.title,
        "content": article.content,
    }

    h1_str = render_to_string("homeview.html", context=context)

    return HttpResponse(h1_str)


def article_detail_view(request, pk):
    # def get(self, request, pk=None):
        article = None
        # print(pk)
        if pk is not None:
            article = Article.objects.get(id=pk)
            # print(article)
        context = {
            "obj": article
        }
        return render(request, "detail.html", context=context)


def article_search_view(request):
    query_dict = request.GET
    query = query_dict.get("q")
    # print(query_dict, query)
    try:
        article = Article.objects.get(id=query)
        # print(article)
        context = {
            "object": article
        }
    except ObjectDoesNotExist:
        context = {}
    return render(request, 'search.html', context=context)


# @login_required
# def article_create_view(request):
#     form = ArticleForm()
#     context = {
#         "form": form
#     }
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             data = request.POST
#             title = data.get("title")
#             content = data.get("content")
#             # print(title, content)
#             # print(title, content)
#             article_object = Article.objects.create(title=title, content=content)
#             created = True
#
#             context = {
#                 "object": article_object,
#                 "created": created
#             }
#     return render(request, 'create.html', context=context)


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        form.save()
        context['created']: True
        context['form'] = ArticleForm()
    return render(request, 'create.html', context=context)




