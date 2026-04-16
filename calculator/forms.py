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
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})


class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'category', 'calories', 'protein', 'carbs', 'fat', 'fiber', 'sugar']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Food Name'}),
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
        label='Select CSV File',
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.csv'})
    )
