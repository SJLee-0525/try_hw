from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm
from .models import Author, Book
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    return render(request, 'libraries/index.html')

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect('accounts:profile', request.user.username)
    else:
        form = AuthorForm()
    context = {
        'form': form,
    }
    return render(request, 'libraries/create_author.html', context)

def books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/books.html', context)

def create_books(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libraries:books')
        pass
    else:
        form = BookForm()
    context = {
        'form': form,
    }
    return render(request, 'libraries/create_books.html', context)