from django.urls import path
from .views import TodoView, TodoDetailView, TodoUpdateView, ToDoDeleteView, TodoCompletedView

urlpatterns = [
    path('todos_get/', TodoView.as_view(), name='todos'),
    path('todos_detail/<str:pk>/', TodoDetailView.as_view(), name='todo_details'),
    path('todo_update/<str:pk>/', TodoUpdateView.as_view(), name='todo_update'),
    path('todo_delete/<str:pk>/', ToDoDeleteView.as_view(), name='todo_delete'),
    path('todo_completed/<str:pk>/', TodoCompletedView.as_view(), name='todo_completed')
]

