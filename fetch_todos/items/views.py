from django.shortcuts import render
from django.views import View
from .forms import ItemForm
# Create your views here.

class TodoList(View):

    def get(self, request):
        form = ItemForm()
        return render(request, "items/todos.html", {"form": form})
