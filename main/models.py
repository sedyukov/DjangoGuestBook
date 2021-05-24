from django.db import models
import datetime
# Create your models here.


class Category(models.Model):
    name = models.CharField('Категория', max_length=50)
    link = models.CharField('Ссылка', max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Review(models.Model):
    author = models.CharField('Автор', max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField('Дата добавления', auto_now_add=True)
    time = models.TimeField('Время обращения', auto_now_add=True)
    text = models.TextField('Текст отзыва')

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return '/'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'