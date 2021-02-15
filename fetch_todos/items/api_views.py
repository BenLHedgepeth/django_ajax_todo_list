
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo

class AddTodoView(APIView):

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            all_todos = TodoSerializer(Todo.objects.all(), many=True)
            return Response(all_todos.data, 200)
