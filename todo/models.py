from django.db import models


class Todo(models.Model):
    todo_title = models.CharField(max_length=100)
