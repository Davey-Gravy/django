from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ToDoList(models.Model):
    # Links ToDoList with User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # properties
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    # links Item with ToDoList
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    # properties
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self) -> str:
        return self.text