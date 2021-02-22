
from django.db import IntegrityError

from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo

class AddTodoView(APIView):

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                todo = serializer.save()
            except IntegrityError:
                return Response(status=204)
            else:
                serializer = TodoSerializer(todo)
                return Response(serializer.data, 200)

class DeleteTodoView(APIView):

    def delete(self, request, id):
        todo = Todo.objects.get(id=id)
        todo.delete()
        return Response(status=204)
