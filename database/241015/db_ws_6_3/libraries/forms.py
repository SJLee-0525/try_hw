from .models import Author, Book
from django import forms

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ('user',)

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'