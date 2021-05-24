from django.contrib.auth.forms import AuthenticationForm
from .models import Review
from django.forms import ModelForm, TextInput, Textarea, Select
from django import forms
from django.contrib.auth.models import User


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'category', 'text']

        widgets = {
            'author': TextInput(attrs={
                'class': 'window__add-name',
                'placeholder': 'Имя, Фамилия'
            }),
            'text': Textarea(attrs={
                'class': 'window__add-text',
                'placeholder': 'Текст отзыва'
            }),
            'category': Select(attrs={
                'class': 'window__add-cat',
            }),
        }


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'window__add-name', 'placeholder': 'Имя пользователя', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'window__add-name-m',
            'placeholder': 'Пароль',
            'id': 'hi',
        }
    )
)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']