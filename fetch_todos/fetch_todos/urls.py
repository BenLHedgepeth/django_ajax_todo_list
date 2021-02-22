"""fetch_todos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

from items import api_views as item_api_views
from items import views as item_views

todos_api = ([
    path("", item_api_views.AddTodoView.as_view(), name="add_todo"),
    path("<int:id>/", item_api_views.DeleteTodoView.as_view(), name="delete_todo"),
], 'items')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", item_views.TodoList.as_view(), name="main_todos"),
    path("api/v1/todos/", include((todos_api), namespace="todos"))
]
