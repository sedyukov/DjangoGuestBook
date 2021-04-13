from .models import Review
from django.forms import ModelForm, TextInput, Textarea, Select


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
