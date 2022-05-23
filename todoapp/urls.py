from django.urls import path

from .views import TodoView, TodoDetailView, TodoUpdateView, ToDoDeleteView, TodoCompletedView,home_view, \
    article_detail_view, article_search_view, article_create_view

from .views_accounts import login_view, logout_view

urlpatterns = [
    path('', home_view, name='home'),
    path('article/<str:pk>', article_detail_view, name='Article_details'),
    path('article_search/', article_search_view, name='Article_search'),
    path('article_create/', article_create_view, name='Article_create'),
    path('login/', login_view, name='Login'),
    path('logout/', logout_view, name='Logout'),

    path('todos_get/', TodoView.as_view(), name='todos'),
    path('todos_detail/<str:pk>/', TodoDetailView.as_view(), name='todo_details'),
    path('todo_update/<str:pk>/', TodoUpdateView.as_view(), name='todo_update'),
    path('todo_delete/<str:pk>/', ToDoDeleteView.as_view(), name='todo_delete'),
    path('todo_completed/<str:pk>/', TodoCompletedView.as_view(), name='todo_completed')
]


