"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from todos import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('todo/', todo_views.todo_list, name='todo_list'),  # Todo list
    path('todo/add/', todo_views.add_todo, name='add_todo'),  # Add Todo
    path('todo/update/<int:pk>/', todo_views.update_todo, name='update_todo'),  # Update Todo
    path('todo/delete/<int:pk>/', todo_views.delete_todo, name='delete_todo'),  # Delete Todo
]

# Custom error handling
handler404 = 'mysite.views.custom_404'
handler500 = 'mysite.views.custom_500'
