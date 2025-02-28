from django.contrib import admin


# todos/admin.py
from django.contrib import admin
from .models import todo

admin.site.register(todo)
