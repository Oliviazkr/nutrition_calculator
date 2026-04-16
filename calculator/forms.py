from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import FoodItem


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': '用户名'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': '邮箱'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': '密码'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': '确认密码'})


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': '用户名'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': '密码'})


class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'category', 'calories', 'protein', 'carbs', 'fat', 'fiber', 'sugar']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '食物名称'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'protein': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'carbs': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'fat': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'fiber': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'sugar': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        }


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(
        label='选择CSV文件',
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.csv'})
    )