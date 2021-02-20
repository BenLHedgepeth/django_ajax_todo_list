
from rest_framework.exceptions import ValidationError
from rest_framework.test import APITestCase
from ..serializers import TodoSerializer
from ..models import Todo

class TestTodoSerializerFail(APITestCase):
    '''Verify that a User is prompted to enter
    a Todo if they fail upon submitting'''


    def setUp(self):
        self.data = {
            'item': "Task Finished"
        }
        self.serializer = TodoSerializer(data=self.data)


    def test_item_field_empty_value(self):
        with self.assertRaisesMessage(ValidationError, "Cannot add a task already completed"):
            self.serializer.is_valid(raise_exception=True)
        total_todos = Todo.objects.count()
        self.assertEqual(total_todos, 0)


class TestTodoSerializerPass(APITestCase):
    '''Verify that a new instance is created'''

    def setUp(self):
        self.data = {
            'item': "Item #1"
        }
        self.serializer = TodoSerializer(data=self.data)
        if self.serializer.is_valid():
            self.serializer.save()

    def test_item_field_empty_value(self):
        total_todos = Todo.objects.count()
        self.assertEqual(total_todos, 1)
        self.assertEqual(self.serializer.data, {'id': 1, 'item': "Item #1"})
