from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    image_description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        )
    )
    class Meta:
        model = Article
        fields = '__all__'