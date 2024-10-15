from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm
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
            return redirect('accounts:profile', author.user.username)
    else:
        form = AuthorForm()
    context = {
        'form': form
    }
    return render(request, 'libraries/create_author.html', context)

def books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/books.html', context)

def books_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libraries:books')
    else:
        form = BookForm()
    context = {
        'form': form
    }
    return render(request, 'libraries/books_create.html', context)

def author_detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    books = author.book_set.all()
    context = {
        'author': author,
        'books': books
    }
    return render(request, 'libraries/author_detail.html', context)