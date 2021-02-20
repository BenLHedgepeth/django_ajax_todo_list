from django.shortcuts import render
from django.views import View
from .forms import ItemForm
from .models import Todo
# Create your views here.

class TodoList(View):

    def get(self, request):
        form = ItemForm()
        todos = Todo.objects.all()
        return render(request, "items/todos.html", {"form": form, "todos": todos})

    def post(self, request):
        form = ItemForm(request.POST)
        return render(request, "items/todos.html", {"form": form})
