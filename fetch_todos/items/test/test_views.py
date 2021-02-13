
from django.test import TestCase
from django.urls import reverse

class TestTodoList(TestCase):

    def test_get_request_todo_list(self):
        response = self.client.get(reverse("main_todos"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "items/todos.html")
