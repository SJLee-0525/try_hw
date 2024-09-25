from django import forms
from .models import Login

class LoginForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'maxlength': 10,
            }
        )
    )

    class Meta:
        model = Login
        fields = '__all__'