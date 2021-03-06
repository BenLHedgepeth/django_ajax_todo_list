
import re
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Todo


class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    item = serializers.CharField(max_length=20)


    def validate_item(self, value):
        regex = re.compile('Completed|Finished|Done')
        if regex.search(value):
            raise ValidationError("Cannot add a task already completed")
        return value

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)
