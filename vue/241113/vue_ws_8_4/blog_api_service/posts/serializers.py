from rest_framework import serializers
from .models import Category, Comment, Post

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('pk', 'title', 'Category')

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'