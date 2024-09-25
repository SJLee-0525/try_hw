from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    price = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={
            'invalid': '올바른 가격을 입력해 주세요. 예: 12.34',
            'max_digits': '가격은 최대 8자리여야 합니다.',
            'max_decimal_places': '가격은 소수점 이하 두 자리여야 합니다.',
        }
    )

    class Meta:
        model = Menu
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '메뉴 이름을 작성해 주세요.'
                    }
                ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '메뉴 설명을 작성해 주세요.'
                    }
                ),
            'is_vegan': forms.RadioSelect(choices=((True, 'Yes'), (False, 'No')), attrs={'class': 'form-check'}),
        }