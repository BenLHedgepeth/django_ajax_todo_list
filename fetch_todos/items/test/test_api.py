
import json
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

class TestAddTodo(APITestCase):

    def setUp(self):
        self.url = reverse("todos:add_todo")
        self.data = json.dumps({"item": "First Todo"})

    def test_new_todo_added(self):
        response = self.client.post(
            self.url, self.data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{'item': "First Todo"}])
