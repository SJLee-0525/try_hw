from django.shortcuts import render
from .models import Author, Book

# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        'authors': authors,
    }
    return render(request, 'libraries/index.html', context)

def detail(request, pk):
    author = Author.objects.get(pk=pk)
    # book = Book.objects.get(pk=pk)
    context = {
        'author': author,
        # 'book': book,
    }
    return render(request, 'libraries/detail.html', context)