
from django.contrib import admin
from django.urls import path, include


# from todoproject.todoapp.models import Task
#
# admin.site.register(Task)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todoapp.urls')),
]

