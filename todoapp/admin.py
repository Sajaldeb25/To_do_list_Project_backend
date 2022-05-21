from django.contrib import admin

from .models import Task, Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Task)
admin.site.register(Article)




