

# todos/models.py
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    class Meta:
        app_label = 'todos'
    def __str__(self):
        return self.title
