from django.urls import path
from .views import TodoView

urlpatterns = [
    path('todos_get/', TodoView.as_view(), name='todos')
]