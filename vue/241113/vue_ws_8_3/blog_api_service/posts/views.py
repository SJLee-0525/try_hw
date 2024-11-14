from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostListSerializer, CategoryCreateSerializer
from .models import Post, Category, Comment

@api_view(['GET'])
def index(request):
    posts = Post.objects.all()
    serializer = PostListSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def category_list_create(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategoryCreateSerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategoryCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)