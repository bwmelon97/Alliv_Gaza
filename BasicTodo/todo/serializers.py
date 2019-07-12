from rest_framework import serializers
from .models import TodoList

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'owner',
            'todo_content',
            'is_completed',
            'pub_date',
            'last_mod',
            'id',
        )
        model = TodoList
