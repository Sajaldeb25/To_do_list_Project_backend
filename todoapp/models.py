from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=400)

    def __str__(self):
        return self.title



