from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    # is_completed = forms.BooleanField(
    #     widget=forms.HiddenInput()        
    #     )

    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {'is_completed': forms.HiddenInput()}