from django.shortcuts import render, redirect
# from .models import Book, Author
# from django.contrib.auth import get_user_model

def index(request):
    return render(request, 'libraries/index.html')