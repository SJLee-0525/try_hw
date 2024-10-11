from django import forms 
from .models import Review, Book

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('content',)