
import json
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

from ..models import Todo

class TestTodo(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.data = {"item": "First Todo"}
        cls.url = reverse("todos:add_todo")
        cls.json = json.dumps(cls.data)

class TestAddTodo(TestTodo):

    def test_new_todo_added(self):
        response = self.client.post(
            self.url, self.json, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 1, 'item': "First Todo"})


class TestDuplicateTodo(TestTodo):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        Todo.objects.create(**cls.data)

    def test_duplicate_todo_added(self):
        response = self.client.post(
            self.url, self.json, content_type="application/json"
        )
        self.assertEqual(response.status_code, 204)
