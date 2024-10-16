from django import forms
from .models import Author, Book


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('nickname', )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'genre')  # author는 자동으로 설정하므로 제외

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            # 요청한 사용자의 저자 인스턴스를 가져옵니다.
            self.author = Author.objects.filter(user=user).first()
            # author 필드는 폼에 포함시키지 않습니다.

    def save(self, commit=True):
        book = super().save(commit=False)
        if hasattr(self, 'author') and self.author:
            book.author = self.author  # 저자 필드에 사용자에 해당하는 저자를 설정
        if commit:
            book.save()
        return book