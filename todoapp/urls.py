from django.urls import path
from .views import TodoView, TodoDetailView, TodoUpdateView

urlpatterns = [
    path('todos_get/', TodoView.as_view(), name='todos'),
    path('todos_detail/<str:pk>/', TodoDetailView.as_view(), name='todo_details'),
    path('todo_update/<str:pk>/', TodoUpdateView.as_view(), name='todo_update')
]

