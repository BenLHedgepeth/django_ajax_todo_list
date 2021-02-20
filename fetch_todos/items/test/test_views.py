
from django.test import TestCase
from django.urls import reverse

from .. models import Todo

class TestTodoList(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.objects = [
            {'item': 'Task #1'},
            {'item': 'Task #2'}
        ]
        for object in cls.objects:
            Todo.objects.create(**object)

    def test_get_request_todo_list(self):
        response = self.client.get(reverse("main_todos"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "items/todos.html")
        self.assertContains(response, "Task #2")
