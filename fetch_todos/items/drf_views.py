
from rest_framework.views import APIView
from .serializers import TodoSerializer

class NewTodoView(APIView):

    def post(self, request):
