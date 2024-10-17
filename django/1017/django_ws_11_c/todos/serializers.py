from rest_framework import serializers
from .models import Todo, Recommend


class TodoSerializer(serializers.ModelSerializer):

    class RecommendSerializerForTodoDetail(serializers.ModelSerializer):
        class Meta:
            model = Recommend
            exclude = ('todo',)

    recommend_set = RecommendSerializerForTodoDetail(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = '__all__'

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('work', 'is_completed', )

class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommend
        fields = '__all__'
        read_only_fields = ('todo',)