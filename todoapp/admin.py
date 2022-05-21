from django.contrib import admin

from .models import Task, Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    # list_display = ['id']  # show id in admin
    # list_display = ['title']  # show title in admin
    list_display = ['title', 'id']  # show both title and id in admin
    search_fields = ['title', 'content']  # search by title and content


admin.site.register(Task)
admin.site.register(Article, ArticleAdmin)




