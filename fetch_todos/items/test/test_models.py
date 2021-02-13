from django.test import TestCase
from ..models import Todo

# Create your tests here.

class TestTodo(TestCase):

    @classmethod
    def setUpTestData(cls):
        data = {
            'item': "Todo #1"
        }
        cls.todo = Todo.objects.create(**data)
        cls.total_todos = Todo.objects.count()

    def test_todo_instance_created(self):
        self.assertIsInstance(self.todo, Todo)
        self.assertEqual(self.todo.item, "Todo #1")
        self.assertEqual(self.total_todos, 1)
